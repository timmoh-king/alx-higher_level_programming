#!/usr/bin/python3

"""Write a function that prints my name"""


def say_my_name(first_name, last_name=""):
    """
        Write a function that prints My name is <first name> <last name>

        Args:
            first_name (str): 1st string
            last_name (str): 2nd string

        Raises:
            TypeError: if name is not string

        Return: My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
