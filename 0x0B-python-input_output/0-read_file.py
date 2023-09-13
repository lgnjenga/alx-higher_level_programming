#!/usr/bin/python3
"""Defines a function that read a text file"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    try:
        with open(filename, encoding="utf-8") as f:
            while True:
                chunk = f.read(1024)  # Read 1 KB at a time
                if not chunk:
                    break
                print(chunk, end="")
    except FileNotFoundError:
        pass  # File doesn't exist, do nothing

# Test the function
if __name__ == "__main__":
    read_file("my_file_0.txt")
