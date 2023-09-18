#!/usr/bin/python3
from models.base import Base
"""Define a class Rectangle"""


class Rectangle(Base):
    """Rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle's position (default is 0).
            y (int): Y-coordinate of the rectangle's position (default is 0).
            id (int): Identifier for the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.

        Args:
            value (int): New width value.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.

        Args:
            value (int): New height value.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Height must be a positive integer")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute.

        Args:
            value (int): New x-coordinate value.
        """
        if not isinstance(value, int):
            raise ValueError("X-coordinate must be an integer")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute.

        Args:
            value (int): New y-coordinate value.
        """
        if not isinstance(value, int):
            raise ValueError("Y-coordinate must be an integer")
        self.__y = value
