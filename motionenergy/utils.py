import numpy as np
def pixel_pitch(
        viewing_distance_cm: float,
        monitor_resolution: tuple[int, int],      # (width_px, height_px)
        monitor_diagonal_inches: float,
) -> tuple[float, int]:
    """
    Pixel Pitch: this is the number of visual degrees per pixel in our stimulus - the
    number of degrees of visual angle needed to differentiate two pixels. This is the inverse
    of the spatial sampling rate.
    To calculate this correctly, we need to go from monitor resolution + size (in pixels/cm),
    and the viewing distance, to the subtended viewing degree angle.
    Iimagine a triangle made by your eye on one side, two pixels on the other.
    half this triangle gives us: tan(0.5𝜽) = 0.5*s / d, where s is the distance
    between two pixels and d is the viewing distance.

    Returns:
        deg_per_pixel : float   – visual degrees subtended by one pixel
        dpi           : int     – dots-per-inch of the monitor (diagonal)
    """
    # physical size of one pixel (assumes square pixels)
    diagonal_cm = monitor_diagonal_inches * 2.54
    diag_pixels = np.hypot(*monitor_resolution)          # √(w²+h²)
    cm_per_pixel = diagonal_cm / diag_pixels

    # visual angle of that pixel
    half_angle_rad = np.arctan((cm_per_pixel / 2) / viewing_distance_cm)
    deg_per_pixel = 2 * np.degrees(half_angle_rad)

    dpi = int(np.round(diag_pixels / monitor_diagonal_inches))
    return deg_per_pixel, dpi