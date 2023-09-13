#!/usr/bin/python3
"""Define a function save_to_json"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to be written to the file.
        filename: The name of the text file to save the object to.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
