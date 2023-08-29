#!/usr/bin/python3
"""Define the class Square."""


class Square:
    """This is the Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the value of the 'size' attribute.

        Returns:
            int: The value of the 'size' attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the 'size aattribute.

        Args:
            value (int): The new value for the 'size' attribute.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the value of the 'position' attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 + integers")
        self.__position = value

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square pattern using the character '#'."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
