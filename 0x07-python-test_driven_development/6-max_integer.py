#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(lst):
    """Find and return the maximum integer in a list of integers.

    Args:
        lst (list): A list of integers.

    Returns:
        int or None: The maximum integer in the list,
        or None if the list is empty.
    """
    if not lst:
        return None

    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num

    return max_num
