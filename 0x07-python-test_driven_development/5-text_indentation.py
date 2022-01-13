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
        char = ['.', '?', ':']

        # Removes space after special chars
        s = 0
        for items in text:
            if items in char:
                if text[s + 1] == " ":
                    text = text[:s + 1] + text[s + 2:]
            else:
                s += 1

        # Cats '\n\n' after the special char with removed space
        s = 0
        for items in text:
            if items in char:
                text = text[:s + 1] + '\n\n' + text[s + 1:]
                s += 3
            else:
                s += 1

        print(text, end='')
