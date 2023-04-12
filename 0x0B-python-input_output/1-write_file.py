#!/usr/bin/python3

"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
        a function that writes a string to a text

        Args:
            filename(str): name of the file
            text(str): the string to be added

        Return:
            the number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return f.tell()
