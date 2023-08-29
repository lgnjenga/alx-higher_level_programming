#!/usr/bin/python3
"""
This module defines a class named Square.
"""


class Square:
    """
    This class represents a simple square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """
        Validates the size attribute.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
