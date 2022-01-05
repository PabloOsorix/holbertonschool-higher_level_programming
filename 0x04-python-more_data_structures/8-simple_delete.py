#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    count = 0
    if key == "":
        return a_dictionary

    if key.isalpha():
        for key_i in a_dictionary:
            if key_i == key:
                count += 1
                break
        if count != 0:
            del a_dictionary[key_i]

        return a_dictionary
