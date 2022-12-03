#!/usr/bin/python3

def max_integer(my_list=[]):

    length = len(my_list)
    if length == 0:
        return None

    my_list.sort()
    max_int = my_list[-1]

    return max_int
