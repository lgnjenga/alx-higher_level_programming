#!/usr/bin/python3
"""
   Defines a function that returns the dictionary description
   with simple data structure
   (list, dictionary, string, integer and boolean)
   for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Convert a Python object to a
    JSON-serializable dictionary description.

    Args:
        obj: An instance of a class
             with serializable attributes.

    Returns:
        dict: A dictionary representation
              of the object suitable for
              JSON serialization.
    """
    # Initialize an empty dictionary
    # to store the JSON representation
    json_dict = {}

    # Get the class attributes
    attributes = obj.__dict__

    # Iterate through the attributes and
    # convert them to JSON-serializable types
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            # If the attribute is a serializable type,
            # add it to the JSON dictionary
            json_dict[key] = value

    return json_dict
