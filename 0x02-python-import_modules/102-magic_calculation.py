#!/usr/bin/python3

def magic_calculation(x, y):
    from magic_calculation_102 import add, sub
    if x < y:
        result = add(x, y)
        for z in range(4, 6):
            result = add(result, z)
        return result
    return sub(x, y)
