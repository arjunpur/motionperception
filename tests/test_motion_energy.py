import numpy as np
import matplotlib
from motionenergy import drifting_sinusoidal, energy, gabor

def test_can_generate_motion_features():
    L = 1
    x, y = np.linspace(0, L, 200), np.linspace(0, L, 200)
    theta = np.pi / 4
    A = 1.0
    f = 2
    phase = 0.0
    frames = 50
    temporal_f = 3

    thetas_deg = np.arange(0, 180, 22.5) # 0 to 180 every 22.5deg
    frequencies = np.array([1.0, 2.0, 4.0]) # cycles/deg
    stimulus = drifting_sinusoidal.sinusoidal_3d(x, y, theta, A, f, temporal_f, frames, phase)
    features = energy.compute_features(stimulus, frequencies, thetas_deg)
    print(features.shape)

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

    # Calculate motion energy for both and check that they are equal
    motion_energy_1 = energy.compute_features(stimulus_1, frequencies, thetas, px_pitch)
    motion_energy_2 = energy.compute_features(stimulus_2, frequencies, thetas, px_pitch)

    assert_energy_rmse_ok(motion_energy_1, motion_energy_2)

def test_motion_energy_spatial_phase_invariance():
    # static stimulus: no temporal drift to test spatial-phase invariance
    speed_deg_sec = 0.0  # no drift
    size_deg = (5.0, 5.0)
    orientation_deg = 45.0
    f_s_cpd = 0.5  # cycles / deg
    amplitude = 1.0
    time = 1.0  # s
    fps = 1.0  # Hz
    px_pitch = 0.02  # deg / pixel

    # generate two stimuli differing only by spatial phase
    phase_1 = 0.0
    phase_2 = np.pi / 2
    stimulus_1 = drifting_sinusoidal.new_stimulus(speed_deg_sec, size_deg, orientation_deg,
                                                  phase_1, f_s_cpd, amplitude, time, fps, px_pitch, log_clock_time=True)
    stimulus_2 = drifting_sinusoidal.new_stimulus(speed_deg_sec, size_deg, orientation_deg,
                                                  phase_2, f_s_cpd, amplitude, time, fps, px_pitch, log_clock_time=True)
    # compute features for both
    frequencies = [0.2, 0.5, 1.0]
    thetas = [0.0, 45.0, 90.0, 135.0]
    motion_energy_1 = energy.compute_features(stimulus_1, frequencies, thetas, px_pitch, verbose=True)
    energy.plot_mean_heatmap(motion_energy_1, frequencies, thetas)
    motion_energy_2 = energy.compute_features(stimulus_2, frequencies, thetas, px_pitch, verbose=True)
    energy.plot_mean_heatmap(motion_energy_2, frequencies, thetas)

    max_kernel_size = 751
    pad = max_kernel_size // 2
    padded_stimulus = np.pad(stimulus_1, [(0, 0), (pad, pad), (pad, pad)], mode='constant')
    # ani = drifting_sinusoidal.animate_stimulus(padded_stimulus, int(time * fps), fps, padded_stimulus.shape[1], padded_stimulus.shape[2], 50, "Padded Stimulus")
    # return ani
    # energies should match despite spatial phase shift
    assert_energy_rmse_ok(motion_energy_1, motion_energy_2)

def assert_energy_rmse_ok(e1, e2):
    tol = 1e-5
    assert e1.shape == e2.shape
    rmse = np.sqrt((e1 - e2) ** 2).mean(axis=0)
    assert rmse.max() < tol, f"root mean squared error was: {rmse.max()}"
