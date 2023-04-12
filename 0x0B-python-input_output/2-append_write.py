#!/usr/bin/python3

"""append a string at the end of textfile"""


def append_write(filename="", text=""):
    """
        appends a string at the end of a text file

        Args:
            filename(str): name of  file
            text(str): text to be appended

        Return:
            return number of characters
    """
    with open(filename, 'a', encoding='utf-8') as f:
        my_file = f.write(text)
        return (my_file)
