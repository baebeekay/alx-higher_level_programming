#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in range(0, len(my_string)):
        if my_string[i] not in "cC":
            new_string += my_string[i]
    return new_string
