#!/usr/bin/python3
"""This Module creates a function to append text to a file"""


def append_write(filename="", text=""):
    """a function to appent text to a file"""
    with open(filename, "a") as f:
        return f.write(text)
