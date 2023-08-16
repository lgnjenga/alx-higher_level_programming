#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Return a new matrix with the square of all the values.
    """
    if not matrix:
        return []

    # Use a list comprehension to create a new matrix
    return [[x ** 2 for x in row] for row in matrix]
