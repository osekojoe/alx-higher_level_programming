#!/usr/bin/python3
"""
Defines a function to add 2 numbers
"""
def add_integer(a, b=98):
    """ Defines a function to add 2 numbers
    Args:
        a: first number
        b: second number
    Returns:
        The sum of two numbers
    Raises:
        TypeError: if a or b are not int or float numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
