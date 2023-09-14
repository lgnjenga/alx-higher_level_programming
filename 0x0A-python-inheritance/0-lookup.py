#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object for which to look up attributes and methods.

    Returns:
        list: A list of attribute and method names.
    """
    # Use the dir() function to get a list of names in the object's namespace
    attributes_and_methods = dir(obj)

    # Filter out names that start with '__'
    # (these are special methods and attributes)
    filtered_names = [
            name for name in attributes_and_methods if not name.startswith(
                '__')]

    return filtered_names
