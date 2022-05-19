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
    for i in range(0, len(list_of_integers), 2):
        if list_of_integers[i] == tmp:
            peak = list_of_integers[i]
            return peak
        tmp = list_of_integers[i] + 2
    if peak == 0:
        for i in list_of_integers:
            if i >= greather:
                greather = i
        return greather


if __name__ == "__main__":
    find_peak()
