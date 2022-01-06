#!/usr/bin/python3


def roman_to_int(roman_string):

    if isinstance(roman_string, str) is False or roman_string is None:
        return(0)
    else:
        num_ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 100}
        counter = 0
        for i in range(len(roman_string) - 1):
            if num_ro[roman_string[i]]\
                    < num_ro[roman_string[i + 1]]:
                counter = counter - num_ro[roman_string[i]]
            else:
                counter = counter + num_ro[roman_string[i]]
        counter = counter + num_ro[roman_string[-1]]
        return(counter)
