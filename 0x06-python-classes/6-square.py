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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Instanse that return total of the Square are,it's public."""
        return self.size * self.size

    def my_print(self):

        if self.size == 0:
            print("")
            return
        [print("") for i in range(0, self.position[1])]
        for i in range(0, self.size):
            [print(" ", end="") for j in range(0, self.position[0])]
            [print("#", end="") for k in range(0, self.size)]
            print("")
