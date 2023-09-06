#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        # Increment the number of instances when a new Rectangle is created
        type(self).number_of_instances += 1
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

    def display(self):
        """Display the Rectangle as a grid of '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for _ in range(self.__height):
            rect.append('#' * self.__width)

        return "\n".join(rect)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return self.display()

    def __repr__(self):
        """Return a string representation of the Rectangle for debugging."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Decrement the number of instances and print a deletion message."""
        # Decrement the number of instances when a Rectangle is deleted
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
