#!/usr/bin/python3
"""
Defines a function for listing an object's attributes.
"""


def lookup(obj):
    """
    Return a list of attributes available for the given object.

    Args:
        obj: The object to list attributes for.

    Returns:
        A list of available attributes.
    """
    return dir(obj)
