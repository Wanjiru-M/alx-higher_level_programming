#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    numbers = [int(arg) for arg in argv[1:]]
    result = sum(numbers)
    print(result)
