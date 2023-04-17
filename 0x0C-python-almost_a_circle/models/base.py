#!/usr/bin/python3

"""define class names base"""


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
