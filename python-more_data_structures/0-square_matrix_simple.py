#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square of all integers in a 2D matrix."""
    return [[x ** 2 for x in row] for row in matrix]
