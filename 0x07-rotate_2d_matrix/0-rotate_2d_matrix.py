#!/usr/bin/python3
"""
A Program that rotates a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):

            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        # Reverse each row for a 90-degree clockwise rotation
        row.reverse()


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)
