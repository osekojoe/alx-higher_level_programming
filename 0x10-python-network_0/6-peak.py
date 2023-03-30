#!/usr/bin/python3
"""Find the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find peak integer"""
    if list_of_integers == [] or list_of_integers is None:
        return None

    least = 0
    high = len(list_of_integers)
    mid = int(((high - least) // 2) + least)

    if high == 1:
        return list_of_integers[0]
    if high == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
