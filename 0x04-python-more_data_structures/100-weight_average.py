#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_mul = sum([x * y for x, y in my_list])
    weight_average = score_mul / sum([y for x, y in my_list])
    return weight_average
