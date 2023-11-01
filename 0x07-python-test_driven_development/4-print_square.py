#!/usr/bin/python3
# 4-print_square.py
"""Defining a square-printing function."""


def print_square(size):
    """
    Print a square made of '#' characters with the given size.

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be greater than or equal to 0")

    for _ in range(size):
        print("#" * size)
