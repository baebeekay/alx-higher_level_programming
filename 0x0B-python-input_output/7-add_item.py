#!/usr/bin/python3
""" 7-add_item.py - module """


# This script that adds all arguments to a Python list,
# and then save them to a file
import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == '__main__':
    """main
    """
    filename = "add_item.json"
    if os.path.isfile(filename):
        listin = load_from_json_file(filename)
        listin += sys.argv[1:]
        save_to_json_file(list(listin), filename)
    else:
        save_to_json_file(sys.argv[1:], filename)
