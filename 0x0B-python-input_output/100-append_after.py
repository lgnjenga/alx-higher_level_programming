#!/usr/bin/python3
"""This script defines a function for inserting text
   after lines containing a specific string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert the specified text after each line containing a
       given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after each found line.
    """
    updated_text = ""

    # Open the file for reading and writing
    with open(filename, "r+") as file:
        for line in file:
            updated_text += line
            if search_string in line:
                updated_text += new_string

        # Move the file cursor to the beginning and truncate the file
        file.seek(0)
        file.truncate()
        file.write(updated_text)

# Example usage:
# append_after("example.txt", "search", "new content to insert")
