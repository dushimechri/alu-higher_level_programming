#!/usr/bin/python3
class Student:
    """Class to define a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize the student with first_name, last_name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance."""
        return self.__dict__
