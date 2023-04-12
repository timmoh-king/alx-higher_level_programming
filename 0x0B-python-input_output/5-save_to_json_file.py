#!/usr/bin/python3

"""a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON rep"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
