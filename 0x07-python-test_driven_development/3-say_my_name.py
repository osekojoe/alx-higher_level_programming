#!/usr/bin/python3
"""Print names
"""


def say_my_name(first_name, last_name=""):
    """ Function print name
    My name is <first name> <last name>
    Args:
        first_name: first name
        last_name: last name
    Raises:
        TypeError: if first_name and last_name are not strings
    Returns:
        My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
