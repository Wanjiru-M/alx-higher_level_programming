#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    print(chr(i), end='')
    print(chr(i - 32), end='')
