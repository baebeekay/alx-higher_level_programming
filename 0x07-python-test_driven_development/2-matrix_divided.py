#!/usr/bin/python3
"""
2-matrix_divided.py, - Divides the given matrix by the
parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by "div"
    checks if the entire list is int/float
    checks if each list in the matrix are the same size
    checks if "div" is an int/float or is 0
    """
    TypeM = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(TypeM)
            else:
                inner_list.append(round(items / div, 2))
        new_matrix.append(inner_list)

    return new_matrix
