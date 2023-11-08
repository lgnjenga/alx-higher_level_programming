#!/usr/bin/python3
"""Defines a function for checking object type."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare obj's type with.

    Returns:
        True if obj is an instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
