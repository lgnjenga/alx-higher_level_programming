#!/usr/bin/python3
# 3-say_my_name.py
"""Defining a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Print a name in the format "My name is {first_name} {last_name}".

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print (default is an empty string).

    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("Both first_name and last_name must be strings")

    print("My name is {} {}".format(first_name, last_name))
