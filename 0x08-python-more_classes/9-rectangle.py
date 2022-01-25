#!/usr/bin/python3

"""This module contain the Rectangle class"""


class Rectangle:
    """Rectangle class have instances width, heght, area
    perimeter and __str__/__repr__"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        self.__height = value

    def perimeter(self):
        """""public instance method that calculate perimeter
        of the rectangle 2*(width + height)"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def area(self):
        """Area of the retangle (width * height)"""
        return self.width * self.height

    def __str__(self):
        str_result = ""
        for i in range(self.height):
            if self.height == 0 or self.width == 0:
                return str_result
            str_result += "{}".format(self.print_symbol) * self.width
            if i != self.height - 1:
                str_result += "\n"
        return str_result

    def __repr__(self) -> str:
        str_repr = "Rectangle({}, {})".format(self.width, self.height)
        return str_repr

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method that compare areas of different Rectangule object"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that equals width and height with size"""
        return cls(size, size)
