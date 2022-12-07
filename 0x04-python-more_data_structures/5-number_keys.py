#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    keys_list = list(a_dictionary.keys())

    for i in keys_list:
        num += 1

    return (num)
