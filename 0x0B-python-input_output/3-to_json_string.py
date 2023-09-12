#!/usr/bin/python3
"""This Module creates a function that returns json"""
import json


def to_json_string(my_obj):
    """a function that returns json from an object"""
    return json.dumps(my_obj)
