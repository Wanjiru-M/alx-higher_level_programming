#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    n = len(argv) - 1

    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(n))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
