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

    txt_cp = text[:]

    for c in ".?:":
        txt_list = txt_cp.split(c)
        txt_cp = ""
        for i in txt_list:
            i = i.strip(" ")
            text_cp = i + c if txt_cp is "" else txt_cp + "\n\n" + i + c

    print(txt_cp[:-3], end="")
