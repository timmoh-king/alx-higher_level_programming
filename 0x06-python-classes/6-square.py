#!/usr/bin/python3

"""Write a class Square that defines a square by"""


class Square:
    """define the self attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        for i in value:
            if not isinstance(value, tuple) and len(value) != 2 and value[i] < 0 and not isinstance(value[i], int):
                raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    """define the method to calculate area"""
    def area(self):
        return (self.__size ** 2)

    """define a function to print # on stdout"""
    def my_print(self):
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
