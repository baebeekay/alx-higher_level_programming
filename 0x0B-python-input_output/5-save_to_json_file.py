#!/usr/bin/python3
"""  5-save_to_json_file.py - module """


import json
""" json module """


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
