#!/usr/bin/python3
"""Rotate a matrix clockwise
"""


def rotate_2d_matrix(matrix):
    """Implements rotate a 2d matrix
    Args:
        matrix (list of list): matrix list rep
    Returns:
        None
    """
    m_len = len(matrix)
    for i in range(m_len):
        for j in range(i, m_len):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        matrix[i].reverse()
