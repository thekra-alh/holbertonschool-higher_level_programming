#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The number to divide by.

    Returns:
        list: A new matrix with all elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        >>> matrix_divided(matrix, float('inf'))
        [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        >>> matrix_divided(matrix, float('-inf'))
        [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = None
    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            try:
                result = round(elem / div, 2)
            except OverflowError:
                result = 0.0
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
