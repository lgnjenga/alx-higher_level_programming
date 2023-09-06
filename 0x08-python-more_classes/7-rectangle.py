#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        num_instances (int): The number of Rectangle instances.
        symbol (str): The symbol used for string representation.
    """

    num_instances = 0
    symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self._width = 0
        self._height = 0
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

        self._width = width
        self._height = height

    def calculate_area(self):
        """Calculate and return the area of the Rectangle."""
        return self._width * self._height

    def calculate_perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        return 2 * (self._width + self._height)

    def display(self):
        """Display the Rectangle as a grid of symbols."""
        if self._width == 0 or self._height == 0:
            return ""

        rect = []
        for _ in range(self._height):
            rect.append(str(self.symbol) * self._width)

        return "\n".join(rect)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return self.display()

    def __repr__(self):
        """Return a string representation of the Rectangle for debugging."""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Deleting a Rectangle...")
