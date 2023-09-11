#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """A base class for geometric shapes"""

    def area(self):
        """Calculate the area of the geometric shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if a value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
