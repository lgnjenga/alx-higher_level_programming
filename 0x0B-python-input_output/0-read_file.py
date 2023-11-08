#!/usr/bin/python3
"""This script defines a function for
   displaying the content of a UTF-8 encoded text file.
"""


def read_file(file_path=""):
    """Read and display the text content of a specified file in UTF-8 encoding.

    Args:
        file_path (str): The path to the text file.

    Returns:
        None
    """
    with open(file_path, encoding="utf-8") as text_file:
        content = text_file.read()
        print(content, end="")

# Example usage:
# read_file("sample.txt")
