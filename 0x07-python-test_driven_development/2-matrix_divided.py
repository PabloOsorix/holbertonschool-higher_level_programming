#!/usr/bin/python3

"""Module that provides the fuunction div to div an array
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by divisor
    (div)

    Args:
        matrix (list of lists (lists of int/floats)): first parameter.
        div (int, float): second parameter.
    Return:
        new list with each lists of matrix divides by div
    """
    """conditional to verify if div is an int/float"""
    counter = None
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if isinstance(div, (float, int)):
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")

    """conditional to verrify that matrix is a list of lists"""
    if isinstance(matrix, (list)):
        if matrix is not None:
            for i in matrix:
                counter = len(matrix[0])
                """conditional that verify that each row
                of matrix have the same length"""
                if counter == len(i):
                    """conditional to verify each element
                    of the matrix be a list"""
                    if isinstance(i, list):
                        for j in i:
                            """conditional to verify each element of the list
                            of the matrix have int or float"""
                            if isinstance(j, (int, float)):
                                continue
                            else:
                                raise TypeError(matrix_error)
                    else:
                        raise TypeError(matrix_error)
                else:
                    raise TypeError("Each row of the \
matrix must have the same size")
        else:
            raise TypeError(matrix_error)
    else:
        raise TypeError(matrix_error)

    return list(map(lambda i: list(map(lambda j:
                round(j / div, 2), i)), matrix))
