#!/usr/bin/python3

"""def is_kind_of_class(obj, a_class):"""


def is_kind_of_class(obj, a_class):
    """
         if the object is an instance of, or if the object is
         an instance of a class that inherited from

         Args:
            obj (object): the object instance
            a_class (class): the parent class

        Return:
            True or false
    """
    if isinstance(obj, a_class):
        return True
    return False
