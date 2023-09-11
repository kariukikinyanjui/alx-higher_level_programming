#!/usr/bin/python3
"""Define a class MyInt"""


class MyInt(int):
    def __eq__(self, other):
        """override the equality operator (==) to invert it"""
        return super().__ne__(other)

    def __ne__(self, other):
        """override the inequality operator (!=) to invert it"""
        return super().__eq__(other)
