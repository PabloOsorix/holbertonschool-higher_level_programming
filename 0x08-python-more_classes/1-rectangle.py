#!/usr/bin/python3

""""Rectangle class with width and height atributes"""


class Rectangle:
    """Rectangle class with atributes width and height"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """property that return the width instance modify
        by the setter"""
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """property that return the height instance modify
        by setter"""
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        
        self._height = value
