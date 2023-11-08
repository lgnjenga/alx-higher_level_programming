#!/usr/bin/python3
"""Defines a function for checking object's class inheritance."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or its subclass.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare obj's type with.

    Returns:
        True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return issubclass(type(obj), a_class)
