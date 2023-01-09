#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """class MyInt"""

    def __eq__(self, value):
        """is equal"""
        return self.real != value

    def __ne__(self, value):
        """is not equal"""
        return self.real == value
