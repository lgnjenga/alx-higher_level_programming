#!/usr/bin/python3
"""This script defines a function for saving a Python object as a JSON file."""
import json


def save_to_json_file(data, filename):
    """Serialize and write a Python object as JSON to a specified file.

    Args:
        data: The Python object to be saved as a JSON file.
        filename (str): The name of the file where the
                        JSON representation will be saved.

    Returns:
        None
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

# Example usage:
# save_to_json_file(
# {"name": "John", "age": 30, "city": "New York"}, "data.json")
