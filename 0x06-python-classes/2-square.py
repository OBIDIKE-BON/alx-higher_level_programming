#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """An empty class called Square"""
    def __init__(self, size=0):
        """Initializes Squares.
        Args:
            size (int): size of the latest square.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
