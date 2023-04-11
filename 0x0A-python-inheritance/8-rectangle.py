#!/usr/bin/python3

"""Write an empty class BaseGeometry"""


class BaseGeometry:
    """define class"""
    def area(self):
        """define area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function that validates value:"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = value


class Rectangle(BaseGeometry):
    """define class attributes"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
