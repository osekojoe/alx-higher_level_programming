#!/usr/bin/python3
""" Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """ Matrix multiplication
    Args:
        m_a: first matrix
        m_b: second matrix
    Raises:
       TypeError: if m_a or m_b is not a list
       TypeError: if m_a or m_b is not a list of lists
       ValueError: if m_a or m_b is empty
       TypeError: if an element is not integer or float
       TypeError: if m_a or m_b rows not equal size
       ValueError: if m_a and m_b cant be multiplied
    Return:
        product matrix
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')

    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    for elem in m_a:
        if not isinstance(elem, list):
            raise TypeError('m_a must be a list of lists')

    for elem in m_b:
        if not isinstance(elem, list):
            raise TypeError('m_a must be a list of lists')

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lst in m_a:
        for elem in lst:
            if not type(elem) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lst in m_b:
        for elem in lst:
            if not type(elem) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """
    mb_inverted = []
    for row in range(len(m_b[0])):
        new_row = []
        for col in range(len(m_b):
            new_row.append(m_b[col][row])
        mb_inverted.append(new_row)

    prodMatrix = []
    for row in m_a:
        new_row = []
        for col in mb_inverted:
            prod = 0
            for i in range(len(mb_inverted[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        prodMatrix.append(new_row)
    """
    prodMatrix = [[0 for x in range(len(m_a[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                prodMatrix[i][j] += m_a[i][k] * m_b[k][j]

    return prodMatrix
