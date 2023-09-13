#!/usr/bin/python3
"""Define a function load_from_json_file"""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename: The name of the JSON file to read.

    Returns:
        object: The Python object rerpresented by the JSON data in the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
