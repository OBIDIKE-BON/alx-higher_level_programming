#!/usr/bin/python3
"""This Module creates a function to read and write"""


def read_file(filename=""):
    """function that reads and print a file"""
    with open(filename, "r") as f:
        print(f.read(), end="")
