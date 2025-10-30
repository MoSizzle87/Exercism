def distance(strand_a, strand_b):
    """Calculate the Hamming distance between two DNA strands.

    :param strand_a: str - first DNA strand.
    :param strand_b: str - second DNA strand.
    :return: int - the Hamming distance between the two strands.
    :raises ValueError: if the strands are not of equal length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming_distance = 0
    for i in range(strand_a):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1

    return hamming_distance
