#!/usr/bin/python3

"""Module contains class BaseGeometry"""


class BaseGeometry:
    """class that raises an Exception with
    the message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
