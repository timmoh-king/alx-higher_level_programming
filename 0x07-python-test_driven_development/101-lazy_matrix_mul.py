#!/usr/bin/python3

"""multiplies 2 matrices by using the module"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
         a function that multiplies 2 matrices

         Args:
            m_a (list of lists of ints/floats): the fist matrix
            m_b (list of lists of ints/floats): the second matrix
    """
    return (np.matmul(m_a, m_b))
