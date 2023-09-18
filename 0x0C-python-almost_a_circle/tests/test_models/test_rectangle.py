#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""Define unittests for square.py"""


class TestRectangle(unittest.TestCase):

    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 1/2 - 4/5")

    def test_update_args(self):
        r = Rectangle(4, 5)
        r.update(10, 2)
        self.assertEqual(str(r), "[Rectangle] (10) 0/0 - 2/5")

    def test_to_dictionary
