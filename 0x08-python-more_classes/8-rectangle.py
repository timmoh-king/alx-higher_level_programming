#!/usr/bin/python3

"""Write an empty class Rectangle that defines a rectangle:"""


class Rectangle:
    """define the self attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width > 0 and self.__height > 0:
            return ((self.__width * 2) + (self.__height * 2))
        else:
            return 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """print the rectangle with the character #"""

        string = ""
        for row in range(self.__height):
            for column in range(self.__width):
                string += str(self.print_symbol)

            if self.__width != 0 and row < (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        """to recreate a new instance by using"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """detects deletion instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
