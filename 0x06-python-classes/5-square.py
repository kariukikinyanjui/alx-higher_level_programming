#!/usr/bin/python3
"""Define the class Square."""


class Square:
    """This is the Square class."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size(int): The size of the square. Defauls to 0.
        """
        self.size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

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
        Sets the value of the 'size' attribute.

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

    def area(self):
        """
        Computes and returns the area of the square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square pattern using the character '#'.

        Prints an empty line if the size is 0.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
