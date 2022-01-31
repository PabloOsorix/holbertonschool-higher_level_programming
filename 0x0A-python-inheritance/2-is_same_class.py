#!/usr/bin/python3

"""Module contains function is_same_class."""


def is_same_class(obj, a_class):
    """This function that
    returns True if the object is exactly an instance
    of the specified class ; otherwise False
    obj (object) to check
    a_class (class) check with obj"""
    if type(obj) == (a_class):
        return True
    return False
