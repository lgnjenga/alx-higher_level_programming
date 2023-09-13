#!/usr/bin/python3
"""Defines a Student python class."""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list of str, optional):
                A list of attribute names to retrieve.
                If provided, only the specified attributes
                will be included in the dictionary.
                Defaults to None, in which case all
                attributes are retrieved.

        Returns:
            dict: A dictionary representation of the student.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {attr: getattr(
                self, attr) for attr in attrs if hasattr(
                    self, attr)}
