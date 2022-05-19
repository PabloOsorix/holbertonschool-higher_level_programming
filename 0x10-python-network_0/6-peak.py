#!/usr/bin/python3
"""
Module that contains function find_peak
"""


def find_peak(list_of_integers):
    """
    function that find the greather number
    """
    if not list_of_integers:
        return None
    tmp = 0
    greather = 0
    peak = 0
#    for index in range(0, len(list_of_integers), 2):
#        if list_of_integers[index] == tmp:
#            peak = list_of_integers[index]
#            return peak
#        tmp = list_of_integers[index] + 2
#    if peak == 0:
#        for index in list_of_integers:
#            if index >= greather:
#                greather = index
#        return greather
    tmp2 = 1
    tmp3 = 1
    counter = 0
    for index in list_of_integers:
        counter += 1
        if index == tmp and index != tmp2 \
        and tmp3 != tmp2 and counter != 2:
            peak = index
            return peak
        if index >= greather:
            greather = index
        tmp = index + 1
        tmp2 = tmp - 1
        tmp3 = tmp2
    return greather

if __name__ == "__main__":
    find_peak()
