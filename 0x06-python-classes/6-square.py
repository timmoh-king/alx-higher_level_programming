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

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        for i in value:
            if (not isinstance(value, tuple) or
                    len(value) != 2 or
                    not all(isinstance(num, int) for num in value) or
                    not all(num >= 0 for num in value)):
                raise TypeError("position must be a tuple of "
                                "2 positive integers")

        self.__position = value

    """define the method to calculate area"""
    def area(self):
        return (self.__size ** 2)

    """define a function to print # on stdout"""
    def my_print(self):
        """Print the square with character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
