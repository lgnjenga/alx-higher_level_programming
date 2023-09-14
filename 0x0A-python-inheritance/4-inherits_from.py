#!/usr/bin/python3
"""Defines the inherits_from function."""


def inherits_from(obj, a_class):
    """
    Check if the object inherits (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj inherits from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
