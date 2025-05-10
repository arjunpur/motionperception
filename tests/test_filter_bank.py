from motionenergy import gabor


def test_can_create_filter_bank():
    thetas = [0, 45, 90, 135, 180]
    frequencies = [0.25, 0.5, 1]  # cycles/deg
    px_pitch = 0.02
    filters = gabor.new_filter_bank(frequencies, thetas, px_pitch)
    assert len(filters) == 2, "must have one array per phase"
    assert len(filters[0]) == len(filters[1]), "each phase array must have the same number of channels"

