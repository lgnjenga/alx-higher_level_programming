#!/usr/bin/python3
"""Defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
       Check if the object is an instance of, or
       inherits from, the specified class.

       Args:
           obj: The object to check.
           a_class: The class to compare with.

       Returns:
           True if obj is an instance of a_class or
           inherits from it, False otherwise.
    """
    if not isinstance(obj, a_class):
        return False
    return True
