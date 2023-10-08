#!/usr/bin/python3
"""This module contains a function that performs element-wise division on a
    matrix.
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide each element of the matrix by.

    Returns:
        list: A new matrix with the results of the division.
    """
    matrix_out = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or matrix == [] or not all(
            isinstance(row, list) for row in matrix) or not all(
                isinstance(ele, (int, float))
                for ele in [num for row in matrix for num in row]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        matrix_out.append([round(i / div, 2) for i in row])

    return matrix_out
