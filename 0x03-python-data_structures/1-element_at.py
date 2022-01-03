#!/usr/bin/python3


def element_at(my_list, idx):
    counter = 0

    if 0 > idx < len(my_list):
        for i in my_list:
            if counter == idx:
                print("Element at index {:d} is {:d}".format(idx, i))
                print("{:d}}".format(counter))
                break
            counter += 1
    else:
        return None
