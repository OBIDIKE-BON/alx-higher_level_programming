#!/usr/bin/python3
"""This Module creates a function writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
