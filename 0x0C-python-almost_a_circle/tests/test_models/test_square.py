import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):       
        self.sqr = Square(10, 0, 0, 1)

    def tearDown(self):
        self.sqr.size = 10
        self.sqr.x = 0
        self.sqr.y = 0
        self.sqr.id = 1

if __name__ == '__main__':
    unittest.main()
