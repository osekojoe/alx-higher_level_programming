#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """ Function prints text with 2 new lines after each ., ? and :
    Args:
        text: text to be printed
    Raise:
        TypeError: if text is not a string
    Return:
        Indented text
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text_cp = text[:]

    for c in ".?:":
        list_text = text_cp.split(c)
        text_cp = ""
        for i in list_text:
            i = i.strip(" ")
            text_cp = i + c if text_cp is "" else text_cp + "\n\n" + i + c

    print(text_cp[:-3], end="")
