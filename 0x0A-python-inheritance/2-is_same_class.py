#!/usr/bin/python3

"""if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """
        returns True if the object is exactly an instance of the
        specified class otherwise False.

        Args:
            obj (object): the object
            a_class (class): the class

        Return: True or False
    """
    if type(obj) == a_class:
        return True
    return False
