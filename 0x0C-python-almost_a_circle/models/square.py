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

    def __str__(self):
        """print the square details"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width)
