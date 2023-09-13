#!/usr/bin/python3
"""Define a function from_json_string"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by JSON string.

    Args:
        my_str: The JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
