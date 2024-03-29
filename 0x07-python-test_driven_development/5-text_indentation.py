#!/usr/bin/python3

"""prints a text with 2 new lines after each of these characters"""


def text_indentation(text):
    """
        function that prints a text with 2 new lines
        after each of these characters: ., ? and :

        Args:
            text (str): the text passed
            split (str): split the buff
            buff (str): a string

        Raises:
            TypeError: if text is not string

        Return: prints a text with 2 new lines after each character:
    """
    buff = ""
    split = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in ".?:":
            buff += i + '\n\n'
        else:
            buff += i
    split = buff.split('\n')
    for letter in split:
        print(letter.strip())
