#!/usr/bin/python3
"""This script defines a class Student."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student instance.

        Args:
            attrs (list): (Optional) A list of attribute names to represent.
                          If provided, only the specified attributes
                          will be included.

        Returns:
            dict: A dictionary containing the requested attributes.
        """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json_data):
        """Replace all attributes of the Student
           instance using provided JSON data.

        Args:
            json_data (dict): A dictionary with
            attribute names and their corresponding values.
        """
        for key, value in json_data.items():
            setattr(self, key, value)

# Example usage:
# student = Student("John", "Doe", 20)
# json_data = {"first_name": "Alice", "last_name": "Smith", "age": 25}
# student.reload_from_json(json_data)
