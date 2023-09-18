#!/usr/bin/python3
"""Define a class Base"""


class Base:
    """Base class for managing id attributes in future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
           id (int): If provided, set the instance's id attribute to the
           given value.
           Otherwise, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
