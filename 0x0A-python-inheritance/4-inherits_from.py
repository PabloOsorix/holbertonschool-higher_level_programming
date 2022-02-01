#!/usr/bin/python3

"""Module that contain function inheritrs_from"""


def inherits_from(obj, a_class):
    """Function that returns True if the object 
    is an instance of a class that inherited 
    (directly or indirectly) from the specified
    class ; otherwise False.
    obj (object) to check
    a_class(class) to check obj
    """
    if type(a) != a_class:
        return True
    return False

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))