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

    def area(self):
        """Retrieves the area of a square.
        Returns:
            the area of a square.
        """
        return (self.__size**2)

    @property
    def size(self):
        """Sets the area of a square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the area of a square.
        Args:
            value
        """

        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
