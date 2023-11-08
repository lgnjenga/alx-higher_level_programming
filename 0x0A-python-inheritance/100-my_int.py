#!/usr/bin/python3
"""Defines a custom integer class, MyInt, with inverted comparison operators."""


class MyInt(int):
    """Custom integer class that inverts equality operators == and !=."""

    def __eq__(self, value):
        """Override the equality operator to behave like inequality."""
        return self.real != value

    def __ne__(self, value):
        """Override the inequality operator to behave like equality."""
        return self.real == value
