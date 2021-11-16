#!/usr/bin/python3
def uppercase(str):
    str1 = ''
    for i in str:
        if(i >= 'a' and i <= 'z'):
            str1 = str1 + chr((ord(i) - 32))
        else:
            str1 = str1 + i
    print("{:s}".format(str1))
