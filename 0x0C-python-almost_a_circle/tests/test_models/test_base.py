#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):

    def test_instance_id_values(self):
        b1 = Base(1)
        b2 = Base(2)
        b4 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b4.id, 12)

if __name__ == '__main__':
    unittest.main()
