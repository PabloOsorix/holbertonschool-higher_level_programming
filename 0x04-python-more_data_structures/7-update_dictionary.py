#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    count = 0

    if key.isalpha():
        for key_i, value_i in a_dictionary.items():
            if key_i == key:
                a_dictionary[key] = value
                count += 1

        if count == 0:
            key = {key: value}
            a_dictionary.update(key)

        return a_dictionary
