#!/usr/bin/python3


def max_integer(my_list=[]):
    max_number = 0

    if my_list:
        for i in my_list:
            if i >= max_number:
                max_number = i
        return max_number
    else:
        return None


my_list = [1, 90, 2, 13, 34, 5, -13, 3]