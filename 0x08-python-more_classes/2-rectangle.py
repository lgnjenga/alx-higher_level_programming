#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.set_dimensions(width, height)

    def get_dimensions(self):
        """Get the dimensions of the Rectangle as a tuple (width, height)."""
        return (self.__width, self.__height)

    def set_dimensions(self, width, height):
        """Set the dimensions of the Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        if width < 0 or height < 0:
            raise ValueError("width and height must be >= 0")
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height)

    width_height = property(get_dimensions, set_dimensions)

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        self.set_dimensions(value, self.__height)

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        self.set_dimensions(self.__width, value)
