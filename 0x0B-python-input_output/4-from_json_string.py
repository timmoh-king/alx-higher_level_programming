#!/usr/bin/python3

"""returns the object representation of an JSON string"""
import json


def to_json_string(my_str):
    """
        object representation of an JSON string

        Args:
            my_str(str): the object

        Return:
            obj representation of JSON
    """
    return json.loads(my_str)
