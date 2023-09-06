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

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method to print a message when an instance is deleted."""
        print(f"Bye rectangle...")

    width_height = property(get_dimensions, set_dimensions)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)

    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # Create a new instance based on representation
    new_rectangle = eval(repr(my_rectangle))

    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
