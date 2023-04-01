#!/usr/bin/python3

"""Write a class Square that defines a square by"""


class Square:
    """define the self attribute"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    """define the method to calculate area"""
    def area(self):
        return (self.__size ** 2)

    """define a function to print # on stdout"""
    def my_print(self):
        for i in range(self.__size):
            print("#")
        print("")
