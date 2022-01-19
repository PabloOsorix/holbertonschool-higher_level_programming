#!/usr/bin/python3

"""Empty class Square that defines a square"""


class Square:
    """Class taClass that defines a square Instantiation with optional size"""
    """Type and value of size arae verificated"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position properly will be equal to the user input tuple,
        if is not a tuble, raise TypeError
        """
        return self._position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Instanse that return total of the Square are,it's public."""
        return self.size * self.size

    def my_print(self):
        """my_print print # * self.size the self.size times, and print
        spaces * self.position, if self.size
        is 0 print a new line
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                if 0 < self.size != 0:
                    print(" " * self.position[0], end="")
                    print("#" * self.size, end="")
                    print()
