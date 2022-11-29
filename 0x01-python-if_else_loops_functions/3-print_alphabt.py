#!/usr/bin/python3
#97,101; 102, 113; 114, 123
for char in list(range(97, 101)) + list(range(102, 113)) + list(range(114, 123)):
    print("{:c}".format(char), end='')
