import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def new_filter_bank(frequencies: list[float], thetas: NDArray[np.floating], px_pitch: float) -> tuple[NDArray, NDArray]:
    """
    Returns a numpy array of dimension 2 x F, where F is the cartesian product of |frequencies x thetas|
    This function constructs a spatio-temporal Gabor filter for each spatial frequency, orientation,
    and organizes the returned array in terms of the two phases: 0 and np.pi/2 to make downstream
    motion energy computation on the quadrature pair easy.
    """
    phases = [0, np.pi / 2]
    kernels = [[], []]  # two phases - quadrature pairs
    channels = [[], []]
    for (i, phase) in enumerate(phases):
        for (j, f) in enumerate(frequencies):
            for (k, theta) in enumerate(thetas):
                # TODO: Normalize the quadrature pair so that their combined energy is 1
                filter = new_spatial_filter(theta, phase, f, px_pitch)
                kernels[i].append(filter)
                channels[i].append((f, theta))

    # Normalize each quadrature pair so that their combined energy (i.e L2 norm) is 1
    # we want each filter to contribute equally.
    for i in range(len(kernels[0])):
        even = kernels[0][i]
        odd = kernels[1][i]
        norm = np.sqrt((even ** 2 + odd ** 2).sum())
        kernels[0][i] /= norm
        kernels[1][i] /= norm

    return kernels, channels


def new_spatial_filter(
        theta_deg: float,  # degrees
        phase: float,
        f_s: float,  # cycle / deg
        pixel_pitch: float,  # deg / px
        n_sigmas: float = 3.0,
) -> NDArray[np.floating]:
    """
    f_s: number of cycles of visual degree (cycle/deg). this gets converted to (cycle/px) when generating the filter
    pixel_pitch: refers to the deg/px. calculated using \theta = 2 * tan(s/2d) where s = distance b/w two pixels, and d is the
                 viewing distance. for smaller values \theta = s/d. the distance b/w two pixels comes from the monitor resolution
                 and the size of the monitor (i.e # pixels on diagonal / length of diagonal)

    Returns:
        - A normalized Gabor kernel
    """
    theta_rad = np.deg2rad(theta_deg)
    # TODO: Understand how bandwidth plays a role in this sigma calculation. I'm currently using a rule of thumb
    sigma_deg = 0.5 / f_s

    # Pixel pitch refers to the number of visual degrees spanned by a single pixel. In the below calculation,
    # sigma is the spread in degrees, pixel_pitch is in degrees/pixel. We are quantizing the visual degrees by the
    # pixel_pitch of the monitor we have - determining how many pixels will be used to cover 3*spread (95%+ of the gaussian)
    # Once we create the coordinate lattice, we return it back to units of degrees so we have a grid of degrees that are one
    # pixel apart.
    radius_px = max(1, int(np.ceil(n_sigmas * sigma_deg / pixel_pitch)))
    coords_deg = np.arange(-radius_px, radius_px + 1) * pixel_pitch  # coordinate system in degrees
    X, Y = np.meshgrid(coords_deg, coords_deg)

    # TODO: Is there a cleaner way to do this rotation in numpy?
    X_rot = X * np.cos(theta_rad) + Y * np.sin(theta_rad)
    Y_rot = -X * np.sin(theta_rad) + Y * np.cos(theta_rad)

    gaussian = np.exp(-(X_rot ** 2 + Y_rot ** 2) / (2 * sigma_deg ** 2))
    sinusoid = np.cos(2 * np.pi * f_s * X_rot + phase)
    kernel = gaussian * sinusoid

    # We want to remove the DC component (0Hz) from the kernel so that when we convolve it
    # with a flat image we don't produce non-zero response everywhere.
    kernel -= kernel.mean()
    return kernel / np.linalg.norm(kernel)


def new_temporal_filter(phase: float, frequency: float):
    pass


def plot_spatial_gabors(gabors: list[NDArray], dpi: float, title: str):
    num_gabors = len(gabors)
    print(f"--> plotting {num_gabors} kernels")
    num_per_row = min(5, num_gabors)
    num_rows = (num_gabors // num_per_row) + int(bool(num_gabors % num_per_row))  # add an extra row if remainder

    print(f"--> plotting {num_rows} rows with {num_per_row} plots per row")

    fig, axs = plt.subplots(num_rows, num_per_row, squeeze=True, figsize=(100, 100), dpi=dpi)
    plt.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0)
    # plt.suptitle(title)
    plt.xlabel("X")
    plt.xlabel("Y")
    idx = 0
    for i in range(num_rows):
        for j in range(num_per_row):
            if idx >= len(gabors):
                break
            ax = axs[i][j]
            plot_gabor(gabors[idx], ax)
            idx += 1

    plt.show()


def plot_gabor(gabor: NDArray, ax):
    ax.imshow(gabor, cmap='gray', origin='lower')
