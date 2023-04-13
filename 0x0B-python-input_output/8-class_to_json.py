#!/usr/bin/python3

"""eturns the dictionary description with simple data structure"""


def class_to_json(obj):
    """obj is an instance of a Class"""
    return obj.__dict__
