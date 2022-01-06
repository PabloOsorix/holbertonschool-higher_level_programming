#!/usr/bin/python3


def roman_to_int(roman_string):

    if isinstance(roman_string, str) is False or roman_string is None:
        return(0)
    roman_string = roman_string.upper()
    roman_number = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
                    "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
                    "D": 500, "CM": 900, "M": 1000}
    counter = 0
    counter_two = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            counter_two = 0
            if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
                counter += 4
                counter_two += 1
                continue
            if roman_string[i] == 'I' and roman_string[i + 1] == 'X':
                counter += 9
                counter_two += 1
                continue
            if roman_string[i] == 'X' and roman_string[i + 1] == 'L':
                counter += 40
                counter_two += 1
                continue
            if roman_string[i] == 'X' and roman_string[i + 1] == 'C':
                counter += 90
                counter_two += 1
                continue
            if roman_string[i] == 'C' and roman_string[i + 1] == 'D':
                counter += 400
                counter_two += 1
                continue
            if roman_string[i] == 'C' and roman_string[i + 1] == 'M':
                counter += 900
                counter_two += 1
                continue
        if roman_number.get(roman_string[i]) is not None and counter_two == 0:
            counter += roman_number.get(roman_string[i])
    return counter
