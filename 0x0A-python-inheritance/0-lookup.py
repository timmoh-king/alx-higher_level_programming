#!/usr/bin/python3

""" a function that returns the list of available att"""


def lookup(obj):
    """
        returns the list of available attributes and methods

        Args:
            obj (object): the object parameter

        Returns: a list object
    """
    return (dir(obj))
