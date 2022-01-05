#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary.copy()
    count = 0

    if key.isalpha():
        for key_i, value_i in new_dict.items():
            if key_i == key:
                new_dict[key] = value
                count += 1

        if count == 0:
            key = {key: value}
            new_dict.update(key)

        return new_dict
