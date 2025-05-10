import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from scipy.signal import fftconvolve
from motionenergy import gabor
from time import perf_counter


def compute_features(stimulus: NDArray[np.floating], frequencies: list[float], thetas: list[float], px_pitch: float = 0.02, verbose: bool = False) -> NDArray[np.floating]:
    # energy
    start = 0.0
    if verbose:
        start = perf_counter()
    # 1/ Create spatial Gabor filter bank (different orientations) - must be in quadrature pairs (phase shifted)
    # TODO: How do the temporal filters fit into the bank?
    # TODO: What is the shape of the energy matrix (2 x F x T x X x Y)
    #
    # 2/ Convolve Gabor filters with stimulus
    #
    # 3/ Compute motion energy
    # For each quadrature pair, compute the non-linear square + sum to compute the local motion energy for that filter pair
    # Do the above for each time slice

    filters = gabor.new_filter_bank(frequencies, thetas, px_pitch)
    (bank_even, bank_odd), channels = filters
    assert (len(bank_even) == len(bank_odd))

    max_kernel_size = max([kernel.shape[0] for kernel in bank_even])
    if verbose:
        print(f"[compute_features] found max kernel size as: {max_kernel_size}")
    pad = max_kernel_size // 2
    padded_stimulus = np.pad(stimulus, [(0, 0), (pad, pad), (pad, pad)], mode='constant')
    T, H, W = stimulus.shape
    energy = np.zeros((T, len(bank_even)))

    # In each frame, how much motion energy is present for a (frequency, theta) pair.
    # Determine this by convolving the Gabor even / odd filter with the stimulus,
    # then computing the energy of the quadrature pair. Take the mean for that frame
    # to get a scalar.
    for kernel_idx in range(len(bank_even)):
        even_filter = bank_even[kernel_idx][::-1, ::-1]
        odd_filter = bank_odd[kernel_idx][::-1, ::-1]
        for (frame_idx, frame) in enumerate(padded_stimulus):
            # TODO: How exactly should I think about the dimensions of the output (how does this change with mode='valid')
            # TODO: How does an FFT Convolve work?
            even = fftconvolve(frame, even_filter, mode="valid")
            odd = fftconvolve(frame, odd_filter, mode="valid")

            local_energy = even ** 2 + odd ** 2

            # TODO: Is the spatial pooling necessary?
            energy[frame_idx, kernel_idx] = local_energy.mean()
    
    if verbose:
        end = perf_counter()
        print(f"[compute_features] took {end-start:.6f}s | "
            f"num_frequencies={len(frequencies)}, num_thetas={len(thetas)}, px_pitch={px_pitch}")

        print(f"[compute_features] outputting energy of shape {energy.shape}")

    return energy

def plot_mean_heatmap(energy: NDArray[np.floating], frequencies: list[float], thetas: list[float]) -> None:
    """Plot a heatmap of the mean motion energy for each (frequency, theta) pair."""
    # Average across time frames
    mean_energy = energy.mean(axis=0)
    num_f = len(frequencies)
    num_t = len(thetas)
    if mean_energy.size != num_f * num_t:
        raise ValueError(f"Energy vector of length {mean_energy.size} cannot be reshaped into ({num_f}, {num_t})")
    # Reshape into (frequencies, thetas)
    heatmap = mean_energy.reshape(num_f, num_t)
    fig, ax = plt.subplots()
    im = ax.imshow(heatmap, aspect='auto', origin='lower', cmap='viridis')
    # Set axis ticks to actual frequency and theta values
    ax.set_xticks(np.arange(num_t))
    ax.set_xticklabels([str(t) for t in thetas])
    ax.set_yticks(np.arange(num_f))
    ax.set_yticklabels([str(f) for f in frequencies])
    ax.set_xlabel('Theta (deg)')
    ax.set_ylabel('Frequency (cycles/deg)')
    ax.set_title('Mean Motion Energy Heatmap')
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label('Energy')
    # annotate heatmap cells with actual energy values
    for i in range(num_f):
        for j in range(num_t):
            value = heatmap[i, j]
            ax.text(j, i, f"{value:.2f}", ha='center', va='center', color='white')
    plt.show()
