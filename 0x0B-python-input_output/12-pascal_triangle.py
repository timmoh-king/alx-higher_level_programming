#!/usr/bin/python3

"""returns a list of lists of integers representing the"""


def pascal_triangle(n):
    """a list of lists of integers representing the Pascal"""
    matrix = []

    if n <= 1:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i+ 1]
        tmp.append(1)
        triangle.append(tmp)
    return triangle
