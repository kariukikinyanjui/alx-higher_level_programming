#!/usr/bin/python3
"""Define a function append_write"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns
    the number of characters added

    Args:
        filename: The name of the text file to append to
        text: The string to be appended to the file

    Returns:
        int: The number of characters added to the file.
    """

    try:
        with open(filename, "a+", encoding="utf-8") as file:
            chars_added = file.write(text)
        return chars_added
    except Exception as e:
        print(f"Error: {e}")
        return 0
