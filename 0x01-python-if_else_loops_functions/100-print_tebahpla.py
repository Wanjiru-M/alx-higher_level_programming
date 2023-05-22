#!/usr/bin/python3
for i in range(122, 96, -2):
    a = i if i % 2 == 0 else i - 32
    print(chr(a), end="")
