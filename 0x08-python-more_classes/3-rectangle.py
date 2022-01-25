#!/usr/bin/python3

"""Module that contain a Rectangle class"""


class Rectangle:
    """Rectangle class that have width, height, area
    perimeter and print the size of rectangle with #
    character"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """property that return the width instance modify
        by the setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property that return the height instance modify
        by setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __str__(self):
        str_result = ""

        for i in range(self.height):
            if self.height == 0 or self.width == 0:
                return str_result
            str_result += "#" * self.width
            if i != self.height - 1:
                str_result += "\n"
        return str_result
