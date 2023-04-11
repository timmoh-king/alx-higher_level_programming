#!/usr/bin/python3

"""Write a class MyList that inherits from list"""


class MyList(list):
    """def print_sorted(self): that prints the list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
