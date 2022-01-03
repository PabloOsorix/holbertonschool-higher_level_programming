#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    new_list = []

    if tuple_a[0] is None:
        tuple_a[0] = 0
    if tuple_a[1] is None:
        tuple_a[1] = 0
    if tuple_b[0] is None:
        tuple_b[0] = 0
    if tuple_b[1] is None:
        tuple_b = 0

    for i in zip(tuple_a, tuple_b):
        new_list += i

    new_list = new_list[0] + new_list[1], new_list[2] + new_list[3]
    return tuple(new_list)
