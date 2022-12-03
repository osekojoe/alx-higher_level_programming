#!/usr/bin/python3
def print_list_integer(my_list=[]):
    ints = [x for x in my_list]
    for i in ints:
        print("{}".format(i))
