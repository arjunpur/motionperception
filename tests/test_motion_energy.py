import numpy as np
import pytest
from motionenergy import drifting_sinusoidal, motion_energy, gabor


def test_motion_energy_stimulus_phase_shifted():
    # Define common stimulus parameters
    speed_deg_sec = 0.5  # deg/sec
    size_deg = (5.0, 5.0)  # deg
    orientation_deg = 45.0  # deg
    f_s_cpd = 0.5  # cycles / deg
    amplitude = 1.0
    time = 2.0  # s
    fps = 60.0  # Hz (cycles / s)
    px_pitch = 0.02  # deg / pixel

    # Create a stimulus
    phase_1_rad = 0.0
    stimulus_1 = drifting_sinusoidal.new_stimulus(speed_deg_sec, size_deg, orientation_deg, phase_1_rad, f_s_cpd,
                                                  amplitude, time, fps, px_pitch)

    # Create the same stimulus phase shifted
    phase_2_rad = np.pi / 2
    stimulus_2 = drifting_sinusoidal.new_stimulus(speed_deg_sec, size_deg, orientation_deg, phase_2_rad, f_s_cpd,
                                                  amplitude, time, fps, px_pitch)

    # Create the features
    frequencies = [0.2, 0.5, 1.0]
    thetas = [0.0, 45.0, 90.0, 135.0]
    filters, _ = gabor.new_filter_bank(frequencies, thetas, px_pitch)
    flattened_filters = [filter for phase in filters for filter in phase]

    # Calculate motion energy for both and check that they are equal
    motion_energy_1 = motion_energy.compute_features(stimulus_1, filters)
    motion_energy_2 = motion_energy.compute_features(stimulus_2, filters)

    assert_energy_rmse_ok(motion_energy_1, motion_energy_2)


def assert_energy_rmse_ok(e1, e2):
    tol = 1e-5
    assert e1.shape == e2.shape
    rmse = np.sqrt((e1 - e2) ** 2).mean(axis=0)
    assert rmse.max() < tol, f"root mean squared error was: {rmse.max()}"
