#!/usr/bin/python3
import unittest
from models.square import Square
"""Define unittests for square.py"""


class TestSquare(unittest.TestCase):

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_str(self):
        s = Square(3, 1, 2, 7)
        self.assertEqual(str(s), "[Square] (7) 1/2 - 3")

    def test_update_args(self):
        s = Square(3)
        s.update(10, 2)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 2")

    def test_to_dictionary(self):
        s = Square(3, 1, 2, 7)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 7, 'size': 3, 'x': 1, 'y': 2})

if __name__ == "__main__":
    unittest.main()
