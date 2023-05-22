#!/usr/bin/python3
for num in range(10):
    for digit in range(num + 1, 10):
        if num < 9:
            print("{:02d}, ".format(num), end='')
        else:
            print("{:02d}".format(num), end='')
        print("{:02d}".format(digit))
