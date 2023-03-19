#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):

    multiple = lambda x: x * number

    return list(map(multiple, my_list))
