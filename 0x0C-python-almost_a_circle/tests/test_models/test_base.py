#!/usr/bin/python3
"""Module for all tests"""
import unittest
from models.base import Base


class TestCases(unittest.TestCase):
    """Class to hold all test fo this module"""

    def setUp(self):
        """sets up test before every execution"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(0)
        self.b4 = Base(123)
        self.b5 = Base(-90)
        self.b6 = Base()
        self.b7 = Base(3)

    def test_base_id(self):
        """testing the ids of class base instances"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 0)
        self.assertEqual(self.b4.id, 123)
        self.assertEqual(self.b5.id, -90)
        self.assertEqual(self.b6.id, 3)

if __name__ == '__main__':
    unittest.main
