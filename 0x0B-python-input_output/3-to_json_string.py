#!/usr/bin/python3
""" 3-to_json_string.py - module """


import json
""" json module """


def to_json_string(my_obj):
    """
    a function that returns the JSON representation of an object (string)
    """
    json.dumps(my_obj)
