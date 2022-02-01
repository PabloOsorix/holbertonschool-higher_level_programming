#!/usr/bin/python3


"""Module contains class BaseGeometry"""


class BaseGeometry():
    """New class with area method and integer validator"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
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
