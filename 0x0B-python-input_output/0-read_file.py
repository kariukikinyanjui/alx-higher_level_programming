#!/usr/bin/python3
"""Define a function read_file"""


def read_file(filename=""):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
