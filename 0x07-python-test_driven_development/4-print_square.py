#!/usr/bin/python3

"""This moudele have the function print_square
that print a patron of # according to their arguments
"""


def print_square(size):
    """This function print a patron with a lenght according
    to size and the size times.
    """
    count = 1
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be and integer")
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >=")
        for i in range(size):
            print("#" * size)
            count += 1
    else:
        raise TypeError("size must be an integer")
