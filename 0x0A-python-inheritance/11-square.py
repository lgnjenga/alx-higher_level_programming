#!/usr/bin/python3
"""Defines a Square class, a subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.validate_and_set("size", size)
        super().__init__(size, size)
        self.__size = size
