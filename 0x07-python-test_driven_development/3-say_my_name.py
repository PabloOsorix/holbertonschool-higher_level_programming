#!/usr/bin/python3

"""This is the module say_my_name"""


def say_my_name(first_name, last_name=""):
    """This function print first and last name if
    both of these are strings.

        Args:
            first_name (str): first argument
            last_name (str): Second argument
        Return:
            None, it prints a string with both args together
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")

    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
