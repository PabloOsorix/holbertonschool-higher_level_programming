#!/usr/bin/python3


"""Module contains class BaseGeometry"""


class BaseGeometry():
    """class that raises an Exception with
    the message area() is not implemented"""
    def area(self):
        """method that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """instance that evaluate value
        name (string) used in the raise exception
        value (int) variable to evaluate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Module that contain class Rectangle"""


class Rectangle(BaseGeometry):
    """Class with inherits from class BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
