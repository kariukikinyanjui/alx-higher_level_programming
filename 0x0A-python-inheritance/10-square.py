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


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a Square instance with size"""

        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
