#!/usr/bin/python3
"""Print the contents of a UTF8 text file to stdout."""


def read_file(filename=""):
    try:
        with open(filename, encoding="utf-8") as f:
            while True:
                chunk = f.read(1024)  # Read 1 KB at a time
                if not chunk:
                    break
                print(chunk, end="")
    except FileNotFoundError:
        pass  # File doesn't exist, do nothing
