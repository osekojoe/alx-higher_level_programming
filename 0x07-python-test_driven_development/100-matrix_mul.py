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

