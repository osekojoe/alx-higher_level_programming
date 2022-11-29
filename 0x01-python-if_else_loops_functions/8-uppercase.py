#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            addendum = 32
        else:
            addendum = 0
        print(":c".format(ord(str[i]) - addendum), end='')
    print()
