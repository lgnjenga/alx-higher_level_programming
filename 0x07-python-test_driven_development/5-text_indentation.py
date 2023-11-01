#!/usr/bin/python3
# 5-text_indentation.py
"""Defining a text-indentation function."""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    line = ""
    for char in text:
        if char in ".?:":
            lines.append(line.strip())
            line = ""
        else:
            line += char

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
        print()
