#!/usr/bin/python3

"""declare class rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
        declare the private attributes

        Args:
            width(int): the rectangle width
            height(int): the rectangle height
            x: parameter x
            y: parameter y
            inherit from the super class
    """
    def __init__(self, width, height, x=0, y=0, id=None):

        """declare the private attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle with character #"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                type(self).__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)
