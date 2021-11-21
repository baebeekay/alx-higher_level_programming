#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    print("{:d} {:s}{:s}".format(a - 1, "argument" if a <= 2 else "arguments",
                                 "." if a == 1 else ":"))
    for i, j in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, j))
