#!/usr/bin/python3
# 0-add_integer.py
"""Definition of integer addition function."""


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.

    If a or b are float numbers, they are cast to integers before addition.

    Args:
        a: An integer or float.
        b: An integer or float (default is 98).

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
