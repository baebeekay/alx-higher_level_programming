#!/usr/bin/python3
""" 4-from_json_string.py - module """


import json
""" json module """


def from_json_string(my_str):
    """
    a function that returns an object
    (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)