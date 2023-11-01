#!/usr/bin/python3
# 2-matrix_divided.py
"""Defining a  matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists of numbers (int or float).
        div (int/float): The divisor.

    Returns:
        A new matrix representing the result of the division.

    Raises:
        TypeError: If the matrix is not a list of lists of numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(
                isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must contain only numbers (int or float)")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("All rows in the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (int or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
