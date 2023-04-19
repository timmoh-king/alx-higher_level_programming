#!/usr/bin/python3

"""Write the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Class Square inherits from Rectangle
        Args:
            size: belongs to the square class
            x: belongs to super class
            y: belongs to super class
            id: belongs to super class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """assign attributes to the class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the width and height property"""
        self.width = value
        self.height = value

    def __str__(self):
        """print the square details"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width)

    def update(self, *args, **kwargs):
        """
            adding the public method that assigns attributes
            Args:
                id: the first element
                size: the second argument
                x: the third argument
                y: the fourth argument
        """
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
            else:
                break

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
            else:
                raise ValueError("Invalid attribute: {key}")
