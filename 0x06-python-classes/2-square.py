#!/usr/bin/python3

"""declare a class square"""


class Square:
    """define the private atttributes"""
    def __init__(self, size=0):
        self.__size = size

    try:
         isinstance(self.__size, int)
    except TypeError:
        raise TypeError("size must be an integer")

    if self.__size < 0:
        try:
            raise ValueError("size must be >= 0")
        except:
            raise
