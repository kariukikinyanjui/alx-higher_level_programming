#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two integers r floats and returns their sum."""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    result = a + b
    return result
