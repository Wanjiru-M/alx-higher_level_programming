#!/usr/bin/python3
def magic_calculation(a, b):
    solution = 0
    try:
        for i in range(1, 3):
            if i > a:
                raise Exception('Too far')
            solution += a ** b / i
    except Exception:
        solution = b + a

    return solution
