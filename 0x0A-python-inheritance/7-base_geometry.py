#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """A base class for geometric shapes"""

    def area(self):
        """Calculate the area of the geometric shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if a value is a positive integer"""
        if type(value) != int:
            raise TypeError(f"{} must be an integer".format(name))
        if value <= 0:
            raise ValueError(f"{} must be greater than 0".format(name))
