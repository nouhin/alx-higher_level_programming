#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function that computes the square value of all integers of a matrix."""
    return [[j**2 for j in i] for i in matrix]
