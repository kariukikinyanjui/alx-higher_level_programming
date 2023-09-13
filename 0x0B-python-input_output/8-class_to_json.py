#!/usr/bin/python3
"""Define a function class_to_json"""


def class_to_json(obj):
    """
    Converts an instance of a class with serializable attributes to
    a dictionary suitable for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object for JSON serialization
    """

    return obj.__dict__
