#!/usr/bin/python3

"""returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
        JSON representation of an object (string)

        Args:
            my_obj(obj): the object

        Return: Json  representation
    """
    return json.dumps(my_obj)
