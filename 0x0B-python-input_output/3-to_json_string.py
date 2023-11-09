#!/usr/bin/python3
"""This script defines a function
   to convert a Python object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """Convert a Python object into its JSON
       representation and return it as a string.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: A JSON representation of the provided object as a string.
    """
    return json.dumps(my_obj)

# Example usage:
# json_string = to_json_string({"name": "John", "age": 30, "city": "New York"})
