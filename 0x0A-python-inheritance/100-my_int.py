#!/usr/bin/python3
"""Defines the MyInt class."""


class MyInt(int):
    """A class that inherits from int and inverts == and != operators."""

    def __eq__(self, other):
        """Override the equality (==) operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality (!=) operator."""
        return super().__eq__(other)
