#!/usr/bin/python3
"""This script defines a function for writing text to a file."""


def write_file(filename="", content=""):
    """Write a provided string to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to write.
        content (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        chars_written = file.write(content)
        return chars_written

# Example usage:
# write_file("output.txt", "This is some sample text.")
