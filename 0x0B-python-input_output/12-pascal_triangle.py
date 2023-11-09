#!/usr/bin/python3
"""This script defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of Pascal's Triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        current_row = triangle[-1]
        next_row = [1]
        for i in range(len(current_row) - 1):
            next_row.append(current_row[i] + current_row[i + 1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle

# Example usage:
# pascal_triangle_data = pascal_triangle(5)
