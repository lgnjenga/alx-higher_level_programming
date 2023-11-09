#!/usr/bin/python3
"""This script defines a function for appending text to a file."""


def append_write(filename="", text=""):
    """Append the specified text to the end of a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The string to be added to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        chars_appended = f.write(text)
        return chars_appended

# Example usage:
# append_write("log.txt", "Appended text for the log.")
