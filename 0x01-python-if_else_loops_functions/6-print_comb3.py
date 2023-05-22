#!/usr/bin/python3
for num in range(8):
    for digit in range(num + 1, 10):
        print("{:d}{:d}".format(num, digit), end=", ")
print("{:d}{:d}".format(num + 1, digit))
