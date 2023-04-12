#!/usr/bin/python3

"""returns the JSON representation of an object (string)"""
import json


def to_json_string(my_str):
    """
        JSON representation of an object (string)

        Args:
            my_str(str): the object

        Return: Obj  representation
    """
    return json.loads(my_str)
