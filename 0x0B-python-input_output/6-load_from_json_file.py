#!/usr/bin/python3
"""
   Defines a function that
   creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Deserialize a JSON file and return the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The Python object represented by the JSON data from the file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
