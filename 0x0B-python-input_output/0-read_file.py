#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to be read.
        Defaults to an empty string.

    Returns:
        None

    Raises:
        None

    Notes:
        This function reads the specified text file
        and prints its contents line by line
        to the standard output (stdout).
        It uses UTF-8 encoding to handle text files.

    Example:
        If you have a text file named "my_file.txt" with the following content:

        ```
        This is line 1
        This is line 2
        ```

        You can use the `read_file` function to print its content as follows:

        ```python
        read_file("my_file.txt")
        ```

        Output:
        ```
        This is line 1
        This is line 2
        ```
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
