#!/usr/bin/python3

"""Empty class Square that defines a square"""


class Square:
    """Class taClass that defines a square Instantiation with optional size"""
    """Type and value of size arae verificated"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """property modify private instance size with value also.
        Setter evaluate if it of int type.
        """
        return self._size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self._size = value

    def area(self):
        """Instanse that return total of the Square are,it's public."""
        return self.size * self.size
