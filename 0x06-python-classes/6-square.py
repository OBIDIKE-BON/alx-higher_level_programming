#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """An empty class called Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Squares.
        Args:
            size (int): size of the latest square.
            position (int, int): The position of the new square.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set the current position of the square."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retrieves the area of a square.
        Returns:
            the area of a square.
        """
        return (self.__size**2)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
