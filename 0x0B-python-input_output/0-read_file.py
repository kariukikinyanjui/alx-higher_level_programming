#!/usr/bin/python3
"""Define a function read_file"""


def read_file(filename=""):
    """Read the contents of a text file and prints them to stdout"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
