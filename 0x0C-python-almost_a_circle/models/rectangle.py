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
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                type(self).__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Args:
            id: 1st argument
            width: 2nd argument
            height: 3rd argument
            x: 4th argument
            y: 5th argument
        """
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.__width = arg
            elif i == 2:
                self.__height = arg
            elif i == 3:
                self.__x = arg
            elif i == 4:
                self.__y = arg
            else:
                break

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value
            else:
                raise ValueError("Invalid attribute: {key}")
