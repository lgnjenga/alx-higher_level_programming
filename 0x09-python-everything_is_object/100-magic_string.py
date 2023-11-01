#!/usr/bin/python3
def magic_string():
    """Generate a magical string containing 'BestSchool'.

    The function keeps track of the number of times it has been called and
    appends 'BestSchool' accordingly.

    Returns:
        str: A string containing 'BestSchool'.
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "BestSchool, " * (magic_string.n - 1) + "BestSchool"
