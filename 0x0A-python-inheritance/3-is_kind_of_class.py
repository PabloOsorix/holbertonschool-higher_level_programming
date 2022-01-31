#!/usr/bin/python3

"""This module conntains is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """This function  returns True if the object is an
    instance of, or if the object is an instance of a
    class that inherited from, the specified class ;
    otherwise False.

    obj (object) to check
    a_class (class) to check obj"""

    if isinstance(obj, a_class):
        return True
    return False
