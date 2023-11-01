#!/usr/bin/python3
"""Defining a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    def __init__(self, first_name):
        self.first_name = first_name

    def __setattr__(self, name, value):
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                "Attribute cannot be set. Only 'first_name' is allowed.")

    def __delattr__(self, name):
        if name == 'first_name':
            raise AttributeError("Attribute 'first_name' cannot be deleted.")
        else:
            super().__delattr__(name)
