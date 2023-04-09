#!/usr/bin/python3

""" def matrix_divided to divide matrix """


def matrix_divided(matrix, div):
    """
        Divide all elements of a matrix by the divider

        Args:
            Matrix (list): the matrix
            div (int/float): the divider

        Raises:
            TypeError: if matrix contains non numbers
            ZeroDivisionError: if the div is equal to 0

        Return: new matrix containing results
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
