#!/usr/bin/python3
"""Define a class LockedClass"""


class LockedClass:
    """
    A class that restricts the creation of new instance attributes,
    allowing only 'first_name'.
    """
    __slots__ = ['first_name']

    def __init__(self):
        pass
