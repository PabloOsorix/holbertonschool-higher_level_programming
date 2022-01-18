#!/usr/bin/python3


from typing import Type


def raise_exception():
    try: 
        raise TypeError
    except TypeError:
        pass