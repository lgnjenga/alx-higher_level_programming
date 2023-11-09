#!/usr/bin/python3
"""This script defines a function to convert a
   Python class instance to a JSON-compatible dictionary.
"""


def class_to_json(obj):
    """Convert a Python class instance to a
       dictionary containing serializable attributes.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary representation of the
              serializable attributes of the object.
    """
    return obj.__dict__

# Example usage:
# json_data = class_to_json(my_class_instance)
