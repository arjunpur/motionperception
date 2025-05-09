import numpy as np
from numpy.typing import NDArray
from scipy.signal import fftconvolve


def compute_features(stimulus: NDArray[np.floating], filters: NDArray) -> NDArray[np.floating]:
    # energy
    # 1/ Create spatial Gabor filter bank (different orientations) - must be in quadrature pairs (phase shifted)
    # TODO: How do the temporal filters fit into the bank?
    # TODO: What is the shape of the energy matrix (2 x F x T x X x Y)
    #
    # 2/ Convolve Gabor filters with stimulus
    #
    # 3/ Compute motion energy
    # For each quadrature pair, compute the non-linear square + sum to compute the local motion energy for that filter pair
    # Do the above for each time slice
    bank_even, bank_odd = filters
    assert (len(bank_even) == len(bank_odd))

    max_kernel_size = max([kernel.shape[0] for kernel in bank_even])
    pad = max_kernel_size // 2
    padded_stimulus = np.pad(stimulus, [(0, 0), (pad, pad), (pad, pad)], mode='reflect')
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

    return energy
