#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    elements = 0
    
    for i in range(x):
        try:
            newList = [val for val in my_list if isinstance(val, (int, float))]
            print("{:d}".format(newList[i]), end="")
            elements += 1
        except (IndexError, ValueError, TypeError):
            break

    print("")
    return elements
