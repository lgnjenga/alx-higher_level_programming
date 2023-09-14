#!/usr/bin/python3
"""
   Implements a function for inspecting
   an object's attributes.
"""


def inspect_object_attributes(obj):
    """
       Retrieve and return a list of attributes
       associated with the given object.
    """
    return dir(obj)
