#!/usr/bin/python3


"""Module that contain class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


"""Module that contains Square class"""


class Square(Rectangle):
    """class with iinherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
