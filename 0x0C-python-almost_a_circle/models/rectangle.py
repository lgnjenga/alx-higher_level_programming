#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, identity=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            identity (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(identity)

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer.")
        if value <= 0:
            raise ValueError("Width must be greater than 0.")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer.")
        if value <= 0:
            raise ValueError("Height must be greater than 0.")
        self.__height = value

    @property
    def x(self):
        """Get or set the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("X must be an integer.")
        if value < 0:
            raise ValueError("X must be 0 or greater.")
        self.__x = value

    @property
    def y(self):
        """Get or set the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("Y must be an integer.")
        if value < 0:
            raise ValueError("Y must be 0 or greater.")
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle's attributes.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            self.update_attributes_from_args(args)
        elif kwargs:
            self.update_attributes_from_kwargs(kwargs)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update_attributes_from_args(self, args):
        """Update attributes based on the provided arguments."""
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

    def update_attributes_from_kwargs(self, kwargs):
        """Update attributes based on the provided keyword arguments."""
        for key, value in kwargs.items():
            setattr(self, key, value)
