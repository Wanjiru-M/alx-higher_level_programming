#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if chr(i) in 'zyxwvutsrqponmlkjihgfedcba':
        print(chr(i), end='')
    if chr(i - 32) in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
        print(chr(i - 32), end='')
