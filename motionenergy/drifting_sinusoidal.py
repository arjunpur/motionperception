import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import perf_counter


# TODO: This function will crash the Jupyter kernel with large inputs - we need to optimize the memory
def new_stimulus(
        speed: float,  # deg/sec,
        size: tuple[float, float],  # degrees of visual angle
        theta_deg: float,  # degrees
        phase: float,  # radians
        spatial_frequency: float,  # cycles/deg,
        amplitude: float,
        time: float,  # sec
        fps: float,  # frames per second
        px_pitch: float,  # deg / pixel
        log_clock_time: bool = False
) -> NDArray[np.floating]:
    theta_rad = np.deg2rad(theta_deg)
    start = 0.0
    if log_clock_time:
        start = perf_counter()

    # total number of frames
    frames = int(np.ceil(time * fps))

    px_per_degree = 1.0 / px_pitch
    x_lim, y_lim = int(np.ceil(size[0] * px_per_degree)), int(np.ceil(size[1] * px_per_degree))
    print(f"Calculated width and height of stimulus in pixels as: {x_lim}, {y_lim}")
    x, y = np.arange(0, x_lim), np.arange(0, y_lim)

    nyquist_limit_spatial = 0.5 * px_per_degree
    if spatial_frequency > 0.8 * nyquist_limit_spatial:
        raise ValueError(
            f"stimulus spatial frequency ({spatial_frequency}) is greater than 0.8 * nyquist limit ({nyquist_limit_spatial}) - select a lower frequency")

    # v = 𝝀_s / 𝝀_t = f_t / f_s, since wavelength in spatial terms is how many degrees per cycle
    # we must ensure the temporal frequency is sufficiently below the nyquist max frequency,
    # otherwise we get aliasing (many different frequencies fit the same sampling - we lose the original signal's frequency!)
    nyquist_limit_temporal = 0.5 * fps
    temporal_frequency = speed * spatial_frequency  # cycles/s
    if temporal_frequency > 0.8 * nyquist_limit_temporal:
        raise ValueError(
            f"stimulus temporal frequency is greater than 0.5* nyquist limit - select lower speed or spatial frequency: {temporal_frequency}")

    # now, calculate the sampled frequencies for our digital signal / sinuosoidal
    # cycles / pixel: sampled spatial frequency
    f_s = spatial_frequency * px_pitch
    # cycles / frame: sampled temporal frequency
    f_t = temporal_frequency / fps

    sinusoidal = sinusoidal_3d(
        x,
        y,
        theta_rad,
        amplitude,
        f_s,
        f_t,
        frames,
        phase,
    )
    if log_clock_time:
        end = perf_counter()
        print(f"new_stimulus took {end-start:.6f}s | spatial_frequency={spatial_frequency}, fps={fps}, px_pitch={px_pitch}")
    return sinusoidal


def animate_stimulus(drifting_sinusodial: NDArray[np.floating], frames: int, fps: float, width_px: int, height_px: int,
                     dpi: int, title: str):
    fig, ax = plt.subplots(figsize=(width_px / dpi, height_px / dpi), dpi=dpi)
    im = ax.imshow(drifting_sinusodial[0], cmap='gray', origin='lower')
    fig.colorbar(im)
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Intensity')
    ax.set_xlim(0, width_px)
    ax.set_ylim(0, height_px)
    ax.set_aspect('equal')

    def update(frame):
        next_frame = drifting_sinusodial[frame]
        im.set_array(next_frame)
        return (im,)

    ani = FuncAnimation(
        fig,
        update,
        frames=frames,
        interval=1.0 / fps,
        blit=True,  # redraw changed parts
    )
    plt.close()
    return ani


def sinusoidal_3d(
        x: NDArray,
        y: NDArray,
        theta: float,  # radians
        A: float,
        f_s: float,  # cycle / px
        f_t: float,  # cycle / frame
        frames: int,
        phase: float,  # dimensionless radians
) -> NDArray[np.floating]:
    f = np.arange(0, frames, 1)
    # We use `ij` indexing here to keep the order of the dimensions
    T, X, Y = np.meshgrid(f, x, y, indexing='ij')
    X_rot = X * np.cos(theta) + Y * np.sin(theta)
    sinusoidal = A * np.cos(2 * np.pi * f_s * X_rot - (2 * np.pi * f_t * T) + phase)
    return sinusoidal
