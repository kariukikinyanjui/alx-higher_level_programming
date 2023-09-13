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

    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object is not serializable")

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool)):
            result[key] = value

        elif isinstance(value, (list, dict)):
            result[key] = class_to_json(value)

    return result
