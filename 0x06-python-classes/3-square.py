#!/usr/bin/python3

"""Write a class Square that defines a square by"""


class Square:
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """declare the self value to size"""
        self.__size = size

    """declare the method to find area"""
    def area(self):
        return (self.__size * self.__size)
