#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """class inheritance"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
