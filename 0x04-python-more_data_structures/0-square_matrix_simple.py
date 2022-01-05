#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    matrix_mapped = [list(map(lambda i: i ** 2, i)) for i in matrix]
    return (matrix_mapped)
