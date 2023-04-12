#!/usr/bin/python3

"""append a string at the end of textfile"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return f.tell()
