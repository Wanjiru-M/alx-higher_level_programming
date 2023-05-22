#!/usr/bin/python3
for num in range(9):
    for digit in range(num + 1, 10):
        print("{:02d}, {:02d}".format(num, digit), end=', ')
print("{:02d}{:02d}".format(num + 1, digit))
