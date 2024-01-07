#!/usr/bin/python3

""" Pascal Triangle """


def pascal_triangle(n):
    """Implements pascal triangle"""
    pascal_tri = [[1]]

    if n == 0:
        return pascal_tri
    elif n > 2:
        n -= 1

    for i in range(n):
        tri = list(range(i + 2))
        tri_size = len(pascal_tri[i])
        for j in range(tri_size):
            right_val = 0
            left_val = 0
            cur_val = pascal_tri[i][j]
            if (j - 1) >= 0:
                left_val = pascal_tri[i][j - 1]
            if (j + 1) < tri_size:
                right_val = pascal_tri[i][j + 1]
            tri[j] = left_val + cur_val
            tri[j + 1] = right_val + cur_val
        pascal_tri.append(tri)
    return (pascal_tri)
