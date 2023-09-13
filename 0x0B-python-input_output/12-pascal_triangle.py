#!/usr/bin/python3
"""Define a function pascal_triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row and returns it as a list
    of lists

    Args:
        n: The number of rows to generate.

    Returns:
        List of lists: Pasca;'s triangle up to nth row.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for a in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for b in range(1, a):
            new_element = prev_row[b - 1] + prev_row[b]
            new_row.append(new_element)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
