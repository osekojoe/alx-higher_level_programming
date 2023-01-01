#!/usr/bin/python3
""" Matrix multiplication"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Matrix multiplication with numpy
    Args:
        m_a: first matrix
        m_b: second matrix        
    Return:
        Matrix
    """
    return (np.matmul(m_a, m_b))
