#!/usr/bin/env python3
def print_last_digit(number):
    if number >= 0:
        lastDig = number % 10
    elif number < 0:
        lastDig = number % -10
        lastDig *= -1

    print("{:d}".format(lastDig), end='')
    return lastDig
