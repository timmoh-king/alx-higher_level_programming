#!/usr/bin/python3

"""Write a function that reads a text file (UTF8)"""


def read_file(filename=""):
    """
        reads a text file (UTF8) and prints it to stdout

        Args:
            filename(string): the name of the file
    """
    with open(filename, encoding = 'utf-8') as f:
        print(f.read(), end="")
