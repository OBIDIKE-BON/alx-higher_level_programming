#!/usr/bin/python3
"""This Module creates a function that returns json"""
import json


def to_json_string(my_obj):
    """a function that returns json from an object"""
    try:
        return json.dumps(my_obj)
    except:
        raise TypeError(f"{my_obj} is not JSON serializable")
