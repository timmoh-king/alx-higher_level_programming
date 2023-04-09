#!/usr/bin/python3

""" Write a function that adds 2 integers """


def add_integer(a, b=98):
    """
        function that adds two integers

        Args:
            a (int/float): 1st number
            b (int/float): 2nd number

        Raises:
            TypeError: If a or b is not integer or float

        Return: sum of a and b
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
