#!/usr/bin/python3
"""Defines a Python function that converts JSON to Object"""
import json


def from_json_string(my_str):
    """
    Return a Python data structure (object) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
