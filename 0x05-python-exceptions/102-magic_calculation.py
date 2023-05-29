#!/usr/bin/python3
def magic_calculation(a, b):
    try:
        result = sum((a ** b) / i for i in range(1, 4) if i > a)
    except:
        result = b + a
    return result
