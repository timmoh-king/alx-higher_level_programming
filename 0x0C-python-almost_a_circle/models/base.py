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
