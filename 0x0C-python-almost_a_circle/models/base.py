#!/usr/bin/python3
"""Module containing the ``Base`` class definition."""
import json


class Base:
    """``Base`` class definition."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes objects of class ``Base``. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of a list."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write a list of objects to a file as json"""
        f_name = cls.__name__
        if list_objs is None or len(list_objs) == 0:
            result = "[]"
        else:
            my_list = []
            for i in list_objs:
                my_list.append(i.to_dictionary())
                result = cls.to_json_string(my_list)
        with open(f"{f_name}.json", 'w') as f:
            f.write(result)

    @staticmethod
    def from_json_string(json_string):
        """returns a list from a json string"""
        if json_string is None:
            return []
        return json.loads(json_string)
