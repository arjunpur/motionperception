"""Motion energy computation using Gabor filter banks."""

import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from scipy.signal import fftconvolve
from motionenergy import gabor
from time import perf_counter
from typing import Tuple


def _pad_stimulus_for_convolution(stimulus: NDArray[np.floating], max_kernel_size: int) -> NDArray[np.floating]:
    """Pad stimulus to handle convolution edge effects.
    
    Args:
        stimulus: Input stimulus array of shape (T, H, W)
        max_kernel_size: Maximum size of kernels in the filter bank
        
    Returns:
        Padded stimulus array
    """
    pad_size = max_kernel_size // 2
    return np.pad(stimulus, [(0, 0), (pad_size, pad_size), (pad_size, pad_size)], mode='constant')


def _compute_quadrature_energy(frame: NDArray[np.floating], 
                              even_filter: NDArray[np.floating], 
                              odd_filter: NDArray[np.floating]) -> float:
    """Compute motion energy from quadrature pair of Gabor filters.
    
    Args:
        frame: Single frame from stimulus
        even_filter: Even-phase Gabor filter (spatially flipped for convolution)
        odd_filter: Odd-phase Gabor filter (spatially flipped for convolution)
        
    Returns:
        Mean motion energy for this frame and filter pair
    """
    # Convolve with quadrature pair
    even_response = fftconvolve(frame, even_filter, mode="valid")
    odd_response = fftconvolve(frame, odd_filter, mode="valid")
    
    # Compute local energy and spatially pool by taking the mean
    local_energy = even_response ** 2 + odd_response ** 2
    return local_energy.mean()


def compute_features(stimulus: NDArray[np.floating], 
                    frequencies: list[float], 
                    thetas: list[float], 
                    px_pitch: float = 0.02, 
                    verbose: bool = False) -> NDArray[np.floating]:
    """Compute motion energy features using Gabor filter bank.
    
    This function creates a bank of Gabor filters at different frequencies and orientations,
    convolves them with the input stimulus, and computes motion energy by combining
    quadrature pairs (even and odd phase filters).
    
    Args:
        stimulus: Input stimulus of shape (T, H, W) where T is time, H is height, W is width
        frequencies: List of spatial frequencies in cycles per degree
        thetas: List of orientations in degrees
        px_pitch: Spatial resolution in degrees per pixel
        verbose: Whether to print timing and debug information
        
    Returns:
        Motion energy array of shape (T, num_filters) where num_filters = len(frequencies) * len(thetas)
    """
    start_time = perf_counter() if verbose else 0.0
    
    # Create spatial Gabor filter bank with quadrature pairs
    filter_bank = gabor.new_filter_bank(frequencies, thetas, px_pitch)
    (even_filters, odd_filters), channels = filter_bank
    
    if len(even_filters) != len(odd_filters):
        raise ValueError("Even and odd filter banks must have the same length")
    
    # Prepare stimulus padding to handle convolution edge effects
    max_kernel_size = max(kernel.shape[0] for kernel in even_filters)
    if verbose:
        print(f"[compute_features] max kernel size: {max_kernel_size}")
    
    padded_stimulus = _pad_stimulus_for_convolution(stimulus, max_kernel_size)
    num_frames, _, _ = stimulus.shape
    num_filters = len(even_filters)
    
    # Initialize energy output array
    energy = np.zeros((num_frames, num_filters))
    
    # Compute motion energy for each quadrature pair and frame
    for filter_idx in range(num_filters):
        # Flip filters spatially for convolution (equivalent to correlation)
        even_filter = even_filters[filter_idx][::-1, ::-1]
        odd_filter = odd_filters[filter_idx][::-1, ::-1]
        
        for frame_idx, frame in enumerate(padded_stimulus):
            energy[frame_idx, filter_idx] = _compute_quadrature_energy(
                frame, even_filter, odd_filter
            )
    
    if verbose:
        end_time = perf_counter()
        print(f"[compute_features] computation time: {end_time - start_time:.6f}s | "
              f"frequencies: {len(frequencies)}, orientations: {len(thetas)}, "
              f"px_pitch: {px_pitch}")
        print(f"[compute_features] output energy shape: {energy.shape}")

    return energy


def plot_mean_heatmap(energy: NDArray[np.floating], 
                     frequencies: list[float], 
                     thetas: list[float]) -> None:
    """Plot a heatmap of the mean motion energy for each (frequency, theta) pair.
    
    Args:
        energy: Motion energy array of shape (T, num_filters)
        frequencies: List of spatial frequencies used
        thetas: List of orientations used
        
    Raises:
        ValueError: If energy dimensions don't match frequency/theta combinations
    """
    # Average across time frames
    mean_energy = energy.mean(axis=0)
    num_frequencies = len(frequencies)
    num_orientations = len(thetas)
    expected_size = num_frequencies * num_orientations
    
    if mean_energy.size != expected_size:
        raise ValueError(
            f"Energy vector length {mean_energy.size} cannot be reshaped into "
            f"({num_frequencies}, {num_orientations}). Expected {expected_size} elements."
        )
    
    # Reshape into (frequencies, thetas) matrix
    energy_matrix = mean_energy.reshape(num_frequencies, num_orientations)
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(energy_matrix, aspect='auto', origin='lower', cmap='viridis')
    
    # Configure axes
    ax.set_xticks(np.arange(num_orientations))
    ax.set_xticklabels([f"{theta:.1f}" for theta in thetas])
    ax.set_yticks(np.arange(num_frequencies))
    ax.set_yticklabels([f"{freq:.2f}" for freq in frequencies])
    
    ax.set_xlabel('Orientation (degrees)')
    ax.set_ylabel('Spatial Frequency (cycles/degree)')
    ax.set_title('Mean Motion Energy Heatmap')
    
    # Add colorbar
    colorbar = fig.colorbar(im, ax=ax)
    colorbar.set_label('Motion Energy')
    
    # Annotate cells with energy values
    for freq_idx in range(num_frequencies):
        for theta_idx in range(num_orientations):
            energy_value = energy_matrix[freq_idx, theta_idx]
            ax.text(theta_idx, freq_idx, f"{energy_value:.2f}", 
                   ha='center', va='center', color='white', fontsize=8)
    
    plt.tight_layout()
    plt.show()
