#!/usr/bin/python3

"""Empty class that defines a square"""


class Square:
    """Class that defines a square with private instance attribute size"""
    """verify if size of area is of the allow type and value"""
    def __intit__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if size < 0:
            print("suze must be >= 0", end="")
            raise ValueError

        self.__size = size
