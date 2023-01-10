#!/usr/bin/python3

"""
returns a list of lists of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Pascal triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        row = []
        row.append(i)

        if len(triangle[i]) > 1:
            prev_len = len(triangle[i]) - 1
            nxt = 1

            for j in range(prev_len):
                total = triangle[i][j] + triangle[i][nxt]
                row.append(total)
                nxt += 1

        row.append(i)
        triangle.append(row)

    return triangle
