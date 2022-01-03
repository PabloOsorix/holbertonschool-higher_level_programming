#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    counter = 0

    if 0 < idx < len(my_list):
        my_list[idx] = element
        return my_list
    else:
        return my_list
