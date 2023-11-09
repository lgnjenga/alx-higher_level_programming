#!/usr/bin/python3
"""This script adds command-line arguments
   to a Python list and saves them to a JSON file.
"""

import sys

# Import the required functions from the respective modules
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Attempt to load data from "add_item.json";
# if the file doesn't exist, initialize an empty list

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

# Extend the list with command-line arguments
items.extend(sys.argv[1:])

# Save the updated list as a JSON representation to "add_item.json"
save_to_json_file(items, "add_item.json")
