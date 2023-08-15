#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix,
        this method rotates it 90 degrees clockwise.
        Return:
           None
    """
    matrix_len = len(matrix)

    for i in range(matrix_len):
        for j in range(matrix_len):
            matrix[i].insert(matrix_len, matrix[j][i])

    for i in range(matrix_len):
        for j in range(matrix_len):
            matrix[i].pop(0)
