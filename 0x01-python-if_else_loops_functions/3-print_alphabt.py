#!/usr/bin/python3
#97,101; 102, 113; 114, 123
for char in range(97, 123):
    if char != 101 and char != 113:
        print("{:c}".format(char), end='')
