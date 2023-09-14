#!/usr/bin/python3
"""Define a function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in
    a specific string in a file.

    Args:
        filename: The name of the file to modify.
        search_string: The string to search for in each line.
        new_string: The line of text to insert after lines containing
        the search string

    Returns:
        None
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
