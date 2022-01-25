#!/usr/bin/python3

"""Rectangle module contain the rectangle class"""


class Rectangle:
    """Rectangle class have instances width, heght, area
    perimeter and __str__/__repr__"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
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

    def __repr__(self) -> str:
        str_repr = "Rectangle({}, {})".format(self.width, self.height)
        return str_repr
