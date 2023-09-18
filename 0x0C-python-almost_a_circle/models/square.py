#!/usr/bin/python3
from models.rectangle import Rectangle
"""Define a class Square(Rectangle)"""


class Square(Rectangle):
    """Square class that inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position (default is 0).
            y (int): Y-coordinate of the square's position (default is 0).
            id (int): Identifier for the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value (int): New size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Custom string representation for Square instances.

        Returns:
            str: String representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
