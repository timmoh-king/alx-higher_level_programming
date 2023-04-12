#!/usr/bin/python3

"""append a string at the end of textfile"""


def append_write(filename="", text=""):
    """
        appends a string at the end of a text file

        Args:
            filename(str): the file name
            text(str): the text

        Return:
            the number of characters added:
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return f.tell()
