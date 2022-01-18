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


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))