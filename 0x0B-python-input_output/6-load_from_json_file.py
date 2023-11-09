#!/usr/bin/python3
"""This script defines a function
   for loading a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Read and create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: A Python object representing the data from the JSON file.
    """
    with open(filename) as json_file:
        loaded_data = json.load(json_file)
        return loaded_data

# Example usage:
# loaded_object = load_from_json_file("data.json")
