#!/usr/bin/python3
"""
   Defines a function that writes an Object to a text file,
   using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serialize an object to JSON format and save it to a text file.

    Args:
        my_obj: The Python object to be serialized to JSON.
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
