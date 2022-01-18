#!/usr/bin/python3


def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        if result != 0:
            print("Inside result: {:.1f}".format(result))
        else:
            result = None
            print("Inside result: {}".format(result))
