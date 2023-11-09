#!/usr/bin/python3
# 6-from_json_string.py
"""This script defines a function
   to convert a JSON string to a Python object.
"""
import json


def from_json_string(my_str):
    """Convert the specified JSON string
       into its Python object representation and return it.

    Args:
        my_str (str): The JSON string to be transformed into a Python object.

    Returns:
        object: A Python object that represents the provided JSON string.
    """
    return json.loads(my_str)

# Example usage:
# python_object = from_json_string(
# '{"name": "Alice", "age": 25, "city": "Los Angeles"}')
