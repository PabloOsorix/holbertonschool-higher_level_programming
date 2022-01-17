#!/usr/bin/python3


from typing import Type


def safe_print_integer(value):

    try:
        if int(value):
            print("{:d}".format(value))
            return True
    except Type:
        return False
