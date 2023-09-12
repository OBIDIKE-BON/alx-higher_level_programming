#!/usr/bin/python3
"""This Module creates a function to write to a file"""


def write_file(filename="", text=""):
    """a function to write to a file"""
    with open(filename, "w") as file:
        return f.write(text)
