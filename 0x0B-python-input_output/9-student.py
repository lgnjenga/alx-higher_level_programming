#!/usr/bin/python3
"""This script defines a class Student."""


class Student:
    """Represents a student with
       first name, last name, and age."""

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

    def to_json(self):
        """Get a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the attributes of the Student.
        """
        return self.__dict__

# Example usage:
# student = Student("John", "Doe", 20)
# student_data = student.to_json()
