#!/usr/bin/python3
"""
Add attribute to an object if it is possible
"""


def add_attribute(an_obj, an_attr, a_value):
    """Add attribute to an object if it is possible
    Args:
        - an_obj: object to add the attribute to
        - an_attr: attribute name
        - a_value: attribute value
    """

    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)
