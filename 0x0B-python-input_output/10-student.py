#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """
    A class representing a student with attributes: first_name, last_name,
    and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided attributes.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representatioin of a Student instance.

        Args:
            attrs: A list of attribute names to retrieve

        Returns:
            dict: A dictionary containing all the attributes of the Student.
        """

        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            return {attr: getattr(self, attr) for attr in attrs if
                    hasattr(self, attr)}
