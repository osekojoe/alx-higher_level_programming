#!/usr/bin/python3
""" Print square
"""


def print_square(size):
    """ function prints a square with the character #
    Args:
        size: size length of the square
    Raise:
        TypeError: if size is not integer
        TypeError: if size is float and less than 0
        ValueError: if size is less than 0
    Return:
        Print square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
