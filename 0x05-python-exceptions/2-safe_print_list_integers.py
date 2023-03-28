#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    elements = 0
    val = [val for val in my_list if isinstance(val, (int, float))]

    for i in range(x):
        try:
            print("{}".format(val[i]), end="")
            elements += 1
        except (IndexError):
            break

    print("")
    return elements
