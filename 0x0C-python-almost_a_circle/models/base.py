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

    @classmethod
    def create(cls, **dictionary):
        """creates a new object from the values in dictionary."""
        if cls.__name__ == "Rectangle":
            obj = cls(2, 6)
        else:
            obj = cls(2)
        obj.update(args=None, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Creates a new instance of the class from the contents of a file."""
        filename = f"{cls.__name__}.json"
        list_objs = []
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as file:
                json_string = file.read()
            list_dictionaries = Base.from_json_string(json_string)
            for dictionary in list_dictionaries:
                obj = cls.create(**dictionary)
                list_objs.append(obj)
            return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves the data of a list (Serialization) of objects to the a CSV
        file.
        """
        class_name = cls.__name__
        filename = "{}.csv".format(class_name)
        if class_name == 'Rectangle':
            fields = ['id', 'width', 'height', 'x', 'y']
        elif class_name == 'Square':
            fields = ['id', 'size', 'x', 'y']
        with open(filename, 'w', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """retrieves objects from a CSV file.
        """
        class_name = cls.__name__
        filename = "{}.csv".format(class_name)
        objs = []
        if class_name == 'Rectangle':
            fields = ['id', 'width', 'height', 'x', 'y']
        elif class_name == 'Square':
            fields = ['id', 'size', 'x', 'y']
        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=fields)
            for row in csv_reader:
                attrs = {}
                for key, value in row.items():
                    attrs[key] = int(value)
                obj = cls.create(**attrs)
                objs.append(obj)
        return objs
