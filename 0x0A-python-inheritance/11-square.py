#!/usr/bin/python3
"""Defines the Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class to represent squares."""

    def __init__(self, size):
        """Initialize a Square instance with a given size.

        Args:
            size (int): The size of the square's sides.
        """
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(
                self.__width, self.__height)
