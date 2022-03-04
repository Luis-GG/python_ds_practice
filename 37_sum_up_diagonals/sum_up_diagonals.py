def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    diag_sum = 0
    loop_count = 0
    other = len(matrix[0]) - 1

    for num in matrix:

        diag_sum += num[loop_count]
        diag_sum += num[other]
        loop_count += 1
        other -= 1

        if loop_count == len(matrix):
            return diag_sum
