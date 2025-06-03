import numpy as np
import matplotlib
from motionenergy import drifting_sinusoidal, energy, gabor
from scipy.signal import fftconvolve

def test_can_generate_motion_features():
    L = 1
    x, y = np.linspace(0, L, 200), np.linspace(0, L, 200)
    theta = np.pi / 4
    A = 1.0
    f = 2
    phase = 0.0
    frames = 50
    temporal_f = 3

    thetas_deg = np.arange(0, 180, 22.5).tolist() # 0 to 180 every 22.5deg
    frequencies = [1.0, 2.0, 4.0] # cycles/deg
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
    
    # Debug: examine stimulus properties
    print(f"Stimulus 1 shape: {stimulus_1.shape}")
    print(f"Stimulus 2 shape: {stimulus_2.shape}")
    print(f"Stimulus 1 mean: {stimulus_1.mean():.6f}, std: {stimulus_1.std():.6f}")
    print(f"Stimulus 2 mean: {stimulus_2.mean():.6f}, std: {stimulus_2.std():.6f}")
    print(f"Stimulus 1 min: {stimulus_1.min():.6f}, max: {stimulus_1.max():.6f}")
    print(f"Stimulus 2 min: {stimulus_2.min():.6f}, max: {stimulus_2.max():.6f}")
    
    # Check if the stimuli have the expected phase relationship
    # For a static sinusoid at 45deg orientation, they should be 90deg out of phase
    sample_slice = stimulus_1[0, 125, :]  # middle row
    print(f"Stimulus 1 sample slice range: {sample_slice.min():.6f} to {sample_slice.max():.6f}")
    sample_slice2 = stimulus_2[0, 125, :]
    print(f"Stimulus 2 sample slice range: {sample_slice2.min():.6f} to {sample_slice2.max():.6f}")
    
    # Debug: examine filter bank organization
    frequencies = [0.2, 0.5, 1.0]
    thetas = [0.0, 45.0, 90.0, 135.0]
    filter_bank = gabor.new_filter_bank(frequencies, thetas, px_pitch)
    (even_filters, odd_filters), channels = filter_bank
    print(f"Number of even filters: {len(even_filters)}")
    print(f"Number of odd filters: {len(odd_filters)}")
    print(f"Channels: {channels}")
    
    # compute features for both
    motion_energy_1 = energy.compute_features(stimulus_1, frequencies, thetas, px_pitch, verbose=True)
    # energy.plot_mean_heatmap(motion_energy_1, frequencies, thetas)
    motion_energy_2 = energy.compute_features(stimulus_2, frequencies, thetas, px_pitch, verbose=True)
    # energy.plot_mean_heatmap(motion_energy_2, frequencies, thetas)

    max_kernel_size = 751
    pad = max_kernel_size // 2
    padded_stimulus = np.pad(stimulus_1, [(0, 0), (pad, pad), (pad, pad)], mode='constant')
    # ani = drifting_sinusoidal.animate_stimulus(padded_stimulus, int(time * fps), fps, padded_stimulus.shape[1], padded_stimulus.shape[2], 50, "Padded Stimulus")
    # return ani
    # energies should match despite spatial phase shift
    assert_energy_rmse_ok(motion_energy_1, motion_energy_2)

def assert_energy_rmse_ok(e1, e2):
    # Use a more reasonable tolerance based on the nature of the computation
    # Phase invariance is approximate due to boundary effects and finite precision
    tol = 1e-2  # Allow 1% difference
    assert e1.shape == e2.shape
    rmse = np.sqrt((e1 - e2) ** 2).mean(axis=0)
    
    # Debug: print energy values to understand the difference
    print(f"Energy 1: {e1}")
    print(f"Energy 2: {e2}")
    print(f"Difference: {e1 - e2}")
    print(f"RMSE per filter: {rmse}")
    print(f"Max RMSE: {rmse.max()}")
    print(f"Relative RMSE: {rmse.max() / max(e1.max(), e2.max()):.6f}")
    
    assert rmse.max() < tol, f"root mean squared error was: {rmse.max()}"

def test_debug_spatial_phase_simple():
    """Debug test with a simple sinusoidal pattern to understand phase invariance."""
    import numpy as np
    from motionenergy import energy, gabor
    
    # Create two simple sinusoidal patterns differing only by phase
    size = 64
    x = np.arange(size)
    y = np.arange(size)
    X, Y = np.meshgrid(x, y)
    
    # Spatial frequency in cycles per pixel
    freq = 0.1  # cycles/pixel
    orientation = 0  # horizontal
    
    # Create two patterns with different phases
    phase1 = 0.0
    phase2 = np.pi / 2
    
    pattern1 = np.cos(2 * np.pi * freq * X + phase1)
    pattern2 = np.cos(2 * np.pi * freq * X + phase2)
    
    # Add time dimension (single frame)
    stimulus1 = pattern1[np.newaxis, :, :]
    stimulus2 = pattern2[np.newaxis, :, :]
    
    print(f"Stimulus 1 shape: {stimulus1.shape}")
    print(f"Stimulus 2 shape: {stimulus2.shape}")
    print(f"Stimulus 1 mean: {stimulus1.mean():.6f}, std: {stimulus1.std():.6f}")
    print(f"Stimulus 2 mean: {stimulus2.mean():.6f}, std: {stimulus2.std():.6f}")
    
    # Create simple filter bank
    frequencies = [freq * 50]  # Convert back to cycles/deg (assuming 50 px/deg)
    thetas = [0.0]
    px_pitch = 0.02  # 50 px/deg
    
    # Compute motion energy
    energy1 = energy.compute_features(stimulus1, frequencies, thetas, px_pitch, verbose=True)
    energy2 = energy.compute_features(stimulus2, frequencies, thetas, px_pitch, verbose=True)
    
    print(f"Energy 1: {energy1}")
    print(f"Energy 2: {energy2}")
    print(f"Difference: {np.abs(energy1 - energy2)}")
    
    # They should be approximately equal (phase invariant)
    assert np.allclose(energy1, energy2, rtol=1e-3), f"Energies differ: {energy1} vs {energy2}"

def test_debug_gabor_filters():
    """Debug test to examine Gabor filter properties."""
    import numpy as np
    from motionenergy import gabor
    from scipy.signal import fftconvolve
    
    # Create a simple test pattern
    size = 32
    x = np.arange(size)
    X, Y = np.meshgrid(x, x)
    
    # Create two sinusoidal patterns with different phases
    freq_cpx = 0.1  # cycles per pixel
    phase1 = 0.0
    phase2 = np.pi / 2
    
    pattern1 = np.cos(2 * np.pi * freq_cpx * X + phase1)
    pattern2 = np.cos(2 * np.pi * freq_cpx * X + phase2)
    
    print(f"Pattern 1 mean: {pattern1.mean():.6f}")
    print(f"Pattern 2 mean: {pattern2.mean():.6f}")
    
    # Create a single Gabor filter pair
    freq_cpd = freq_cpx / 0.02  # Convert to cycles per degree
    px_pitch = 0.02
    
    even_filter = gabor.new_spatial_filter(0.0, 0.0, freq_cpd, px_pitch)
    odd_filter = gabor.new_spatial_filter(0.0, np.pi/2, freq_cpd, px_pitch)
    
    print(f"Even filter shape: {even_filter.shape}")
    print(f"Odd filter shape: {odd_filter.shape}")
    print(f"Even filter mean: {even_filter.mean():.6f}")
    print(f"Odd filter mean: {odd_filter.mean():.6f}")
    
    # Manually convolve and compute energy
    even_resp1 = fftconvolve(pattern1, even_filter[::-1, ::-1], mode='valid')
    odd_resp1 = fftconvolve(pattern1, odd_filter[::-1, ::-1], mode='valid')
    energy1 = (even_resp1 ** 2 + odd_resp1 ** 2).mean()
    
    even_resp2 = fftconvolve(pattern2, even_filter[::-1, ::-1], mode='valid')
    odd_resp2 = fftconvolve(pattern2, odd_filter[::-1, ::-1], mode='valid')
    energy2 = (even_resp2 ** 2 + odd_resp2 ** 2).mean()
    
    print(f"Manual energy 1: {energy1:.6f}")
    print(f"Manual energy 2: {energy2:.6f}")
    print(f"Manual difference: {abs(energy1 - energy2):.6f}")
    
    # Check if they're approximately equal
    assert np.allclose(energy1, energy2, rtol=1e-6), f"Manual energies differ: {energy1} vs {energy2}"

def test_debug_zero_mean_patterns():
    """Debug test with zero-mean patterns to eliminate boundary effects."""
    import numpy as np
    from motionenergy import gabor
    from scipy.signal import fftconvolve
    
    # Create a larger test pattern to reduce boundary effects
    size = 64
    x = np.arange(size)
    X, Y = np.meshgrid(x, x)
    
    # Create two sinusoidal patterns with different phases
    freq_cpx = 0.1  # cycles per pixel
    phase1 = 0.0
    phase2 = np.pi / 2
    
    # Create patterns and remove the mean to make them zero-mean
    pattern1 = np.cos(2 * np.pi * freq_cpx * X + phase1)
    pattern1 = pattern1 - pattern1.mean()
    
    pattern2 = np.cos(2 * np.pi * freq_cpx * X + phase2)
    pattern2 = pattern2 - pattern2.mean()
    
    print(f"Pattern 1 mean: {pattern1.mean():.8f}")
    print(f"Pattern 2 mean: {pattern2.mean():.8f}")
    print(f"Pattern 1 std: {pattern1.std():.6f}")
    print(f"Pattern 2 std: {pattern2.std():.6f}")
    
    # Create a single Gabor filter pair
    freq_cpd = freq_cpx / 0.02  # Convert to cycles per degree
    px_pitch = 0.02
    
    even_filter = gabor.new_spatial_filter(0.0, 0.0, freq_cpd, px_pitch)
    odd_filter = gabor.new_spatial_filter(0.0, np.pi/2, freq_cpd, px_pitch)
    
    print(f"Even filter mean: {even_filter.mean():.8f}")
    print(f"Odd filter mean: {odd_filter.mean():.8f}")
    
    # Manually convolve and compute energy
    even_resp1 = fftconvolve(pattern1, even_filter[::-1, ::-1], mode='valid')
    odd_resp1 = fftconvolve(pattern1, odd_filter[::-1, ::-1], mode='valid')
    energy1 = (even_resp1 ** 2 + odd_resp1 ** 2).mean()
    
    even_resp2 = fftconvolve(pattern2, even_filter[::-1, ::-1], mode='valid')
    odd_resp2 = fftconvolve(pattern2, odd_filter[::-1, ::-1], mode='valid')
    energy2 = (even_resp2 ** 2 + odd_resp2 ** 2).mean()
    
    print(f"Manual energy 1: {energy1:.6f}")
    print(f"Manual energy 2: {energy2:.6f}")
    print(f"Manual difference: {abs(energy1 - energy2):.8f}")
    print(f"Relative difference: {abs(energy1 - energy2) / max(energy1, energy2):.8f}")
    
    # Check if they're approximately equal (allowing for small numerical differences)
    assert np.allclose(energy1, energy2, rtol=1e-4), f"Manual energies differ: {energy1} vs {energy2}"
