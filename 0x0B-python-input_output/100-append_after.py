#!/usr/bin/python3
"""  100-append_after.py - module"""


def append_after(filename="", search_string="", new_string=""):
    """Write a function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, mode='r', encoding='UTF8') as f:
        text = ""
        for i in f:
            if search_string in i:
                text += i + new_string
            else:
                text += i
    with open(filename, mode='w', encoding='UTF8') as f:
        f.write(text)
