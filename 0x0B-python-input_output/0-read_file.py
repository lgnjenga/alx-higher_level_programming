#!/usr/bin/python3
"""Print the contents of a UTF8 text file to stdout."""


def read_file(filename=""):
    """Print the contents of a text file"""
    with open(filename, encoding="utf-8") as file_text:
        print(file_text.read(), end="")
