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
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(filename, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string + "\n")
    except Exception as e:
        print(f"Error: {e}")
