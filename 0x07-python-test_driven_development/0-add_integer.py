#!/usr/bin/python3
"""Contains a function to add two integers"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a (int or double): first number.
        b (int or double): second number.
    Returns:
        sum of a and b.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
