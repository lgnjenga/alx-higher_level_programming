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

    def set_dimensions(self, width, height):
        """Set the dimensions of the rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Width and height must be integers")
        if width < 0 or height < 0:
            raise ValueError("Width and height must be >= 0")

        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height)

    def draw(self):
        """Draw the Rectangle using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for _ in range(self.__height):
            rect.append('#' * self.__width)

        return "\n".join(rect)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return self.draw()

    def __repr__(self):
        """Return a string representation of the Rectangle for debugging."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a Rectangle is deleted."""
        print("Bye rectangle...")
