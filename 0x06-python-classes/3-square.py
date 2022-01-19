#!/usr/bin/python3

"""Empty class Square that defines a square"""


class Square:
    """Class taClass that defines a square Instantiation with optional size"""
    """Type and value of size arae verificated"""

    total_size = 0

    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = size
        Square.total_size = size

    def area(self):
        """Instanse that return total of the Square are,it's public."""
        self.area = Square.total_size * Square.total_size
        return self.area
