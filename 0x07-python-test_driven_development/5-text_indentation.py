#!/usr/bin/python3

"""prints a text with 2 new lines after each of these characters"""


def text_indentation(text):
    """
        function that prints a text with 2 new lines
        after each of these characters: ., ? and :

        Args:
            text (str): the text passed

        Raises:
            TypeError: if text is not string

        Return: prints a text with 2 new lines after each character:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (text[i] == "." or text[i] == "?" or text[i] == ":"):
            print("")
            print("")
    print(text)
