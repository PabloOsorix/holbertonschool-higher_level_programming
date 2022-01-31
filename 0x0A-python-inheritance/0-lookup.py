#!/usr/bin/python3

"""This module have lookup function"""


def lookup(obj):
    """This function return a returns
    the list of available attributes
    and methods of an object:
        obj (object) = object to obtain
        their attibutes."""
    return(list(dir(obj)))
