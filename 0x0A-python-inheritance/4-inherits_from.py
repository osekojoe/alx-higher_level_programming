#!/usr/bin/python3
"""
a function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the
specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """check if obj is instance of a class"""
    if isinstance(obj, a_class):
        if issubclass(a_class, obj.__class__) is not True:
            return True
    return False
