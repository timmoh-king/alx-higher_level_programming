#!/usr/bin/python3

"""Prototype: def inherits_from(obj, a_class):"""


def inherits_from(obj, a_class):
    """
        Write a function that returns True if the object is an instance
        of a class that inherited (directly or indirectly) from the
        specified class ; otherwise False.
    """
    if not isinstance(obj, a_class):
        return False
    return True
