#!/usr/bin/python3

"""Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """declare the class attributes"""
    def __init__(self, size):

        """initialize new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
