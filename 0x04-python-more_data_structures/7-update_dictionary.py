#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary.copy()
    for key_i, value_i in new_dict.items():
        if key_i == key:
            new_dict[key] = value
    return new_dict
