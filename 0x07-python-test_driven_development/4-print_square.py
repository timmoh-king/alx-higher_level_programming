#!/usr/bin/python3

"""a function that prints a square with the character #"""


def print_square(size):
    """
        prints a square with the character #

        Args:
            size (int): size length of the square

        Exception:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        Return: prints a square with the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
