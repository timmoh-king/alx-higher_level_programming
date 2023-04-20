#!/usr/bin/python3

"""define class names base"""
import json


class Base:
    """define private class attributes"""
    __nb_objects = 0

    """define the class constructor"""
    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON representation of list to a file"""
        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                obj_dicts = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(obj_dicts)
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string repr json_string:"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if dictionary and dictionary is not {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            elif cls.__name__ == "Square":
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances:"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode="r") as f:
                json_str = f.read()
                obj_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []
