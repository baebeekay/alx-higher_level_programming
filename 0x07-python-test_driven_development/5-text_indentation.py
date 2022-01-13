#!/usr/bin/python3
""" 5-text_indentation.py - indentation module """


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Parameter: text must be a string
    Raise: TypeError with the message "text must be a string"
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        char = ":"
        for i in text:
            if i == " " and char in ".?:":
                continue
            print(i, end="")
            if i in ".:?":
                print("\n")
                char = i
