#!/usr/bin/python3
"""Defines a function to dynamically add attributes to objects."""


def add_attribute(obj, attribute, value):
    """Dynamically add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        attribute (str): The name of the attribute to add to obj.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Unable to add a new attribute to this object.")
    setattr(obj, attribute, value)
