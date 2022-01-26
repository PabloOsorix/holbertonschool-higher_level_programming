#!/usr/bin/python3

"""Function that realice the sum of two integers"""


def add_integer(a, b=98):
    """This function return the sum of arguments a and b
    a and b just can be integers or floats

    Args:
        a (int, float): fisrt arameter.
        b (int, float): second parameter.

    Returns:
        Integer: the sum of parameters a and b, if one
        of these are float it will be casted to int.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if isinstance(a, (float, int)):
        if isinstance(a, float):
            a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (float, int)):
        if isinstance(b, (float)):
            b = int(b)
    else:
        raise TypeError("b must be and integer")
    return a + b
