#!/usr/bin/python3
"""Defines a function that appends to a file"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a UTF8 text file
    and return the number of characters added.

    Args:
        filename (str): File name to append to.
        text (str): The string to append to file.
    Returns:
        Number of characters appended.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        nb_characters_added = f.write(text)
    return nb_characters_added
