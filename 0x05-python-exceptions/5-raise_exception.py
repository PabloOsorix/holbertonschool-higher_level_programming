#!/usr/bin/python3


def rraise_exception():
    try:
        raise TypeError
    except TypeError:
        raise
