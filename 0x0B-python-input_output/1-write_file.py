#!/usr/bin/python3

"""
function that writes a string to a text file (UTF8) and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """
    write string to txt file
    Args:
        filename: file
        text: text to write
    """
    with open(filename, 'w', encoding ='UTF-8') as tf:
        return tf.write(text)
