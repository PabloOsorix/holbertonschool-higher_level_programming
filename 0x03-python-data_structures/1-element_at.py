#!/usr/bin/python3


def element_at(my_list, idx):
    counter = 0

    if 0 > idx < len(my_list):
        for i in my_list:
            if counter == idx:
                return idx, i
            counter += 1
    else:
        return None
