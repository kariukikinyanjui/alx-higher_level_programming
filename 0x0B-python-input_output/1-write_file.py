#!/usr/bin/python3
"""Define a function write_file"""


def write_file(filename="", text=""):
    """
    Writes a string t a text file (UTF8) and returns the number
    of characters written
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            chars_written = file.write(text)
        return chars_written
    except Exception as e:
        print(f"Error: {e}")
        return 0
