#!/usr/bin/python3
import unittest
from models.base import Base
"""Define unittests for base.py"""


class TestBase(unittest.TestCase):

    def test_base_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == "__main__":
    unittest.main()
