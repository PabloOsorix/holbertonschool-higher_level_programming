#!/usr/bin/python3


"""Module that contains Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class with iinherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        new_str = ""
        new_str = "[Square] {}/{}".format(str(self.__size),
                                          str(self.__size))
        return new_str
