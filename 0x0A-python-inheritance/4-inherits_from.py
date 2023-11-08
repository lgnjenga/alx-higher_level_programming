#!/usr/bin/python3
"""Defines a function for checking class inheritance."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare obj's type with.

    Returns:
        True if obj is an inherited instance of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
