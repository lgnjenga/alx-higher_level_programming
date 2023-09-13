#!/usr/bin/python3
"""
   adds all arguments to a Python list,
   and then save them to a file
"""
import sys
import os.path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Check if the JSON file exists
json_filename = "add_item.json"
if os.path.exists(json_filename):
    # Load the existing list from the JSON file
    my_list = load_from_json_file(json_filename)
else:
    # Create a new list if the file doesn't exist
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list as a JSON representation in the file
save_to_json_file(my_list, json_filename)
