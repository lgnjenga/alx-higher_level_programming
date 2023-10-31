#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    This class represents a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.set_dimensions(width, height)

    def set_dimensions(self, width, height):
        """Set the dimensions (width and height) of the Rectangle."""
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Dimensions must be integers")
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.set_dimensions(value, self.__height)

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.set_dimensions(self.__width, value)

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height)

    def display(self):
        """Display the Rectangle using the specified print symbol."""
        for _ in range(self.__height):
            print(str(self.print_symbol) * self.__width)

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = [str(
                self.print_symbol) * self.__width for _ in range(
                    self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
