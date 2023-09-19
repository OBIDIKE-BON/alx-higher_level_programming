#!/usr/bin/python3
"""Module containing ``Square`` class definition."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """``Square`` class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instance of ``Square`` class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of instance."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """public ``size`` property getter"""
        return self.width

    @size.setter
    def size(self, size):
        """public ``size`` property settet"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates each attribute of the class."""
        attr = ['id', 'size', 'x', 'y']
        lent = len(args)

        if args is not None and lent != 0:
            for i in range(lent):
                setattr(self, attr[i], args[i])
        else:
            for x in list(kwargs.keys()):
                setattr(self, x, kwargs(x))
