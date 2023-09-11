#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Methods:
    - area(): Raises an exception with the message "area() is not implemented"
    - integer_validator(name, value): Validates if a value is a positive int

    Attributes:
    - No additional attributes.
    """

    def area(self):
        """Calculate the area of the geometric shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if a value is a positive integer"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""Define a class Rectangle"""


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height"""

        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """Return a string representation of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
