#!/usr/bin/python3
import unittest
from models.base import Base
"""Define unittests for base.py"""


class TestBase(unittest.TestCase):

    def test_base_auto_assign_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_auto_increment_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_save_id_passed(self):
        b = Base(89)
        self.assertEqual(b.id, 89)


if __name__ == "__main__":
    unittest.main()
