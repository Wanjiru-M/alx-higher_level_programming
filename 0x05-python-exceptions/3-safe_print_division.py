#!/usr/bin/python3
def safe_print_division(a, b):
    solution = None
    try:
        solution = a / b
    except ZeroDivisionError:
        pass
    finally:
        if solution is None:
            print("Inside result: None")
        else:
            print("Inside result: {}".format(solution))
    return solution
