#!/usr/bin/python3
import sys

def safe_function(function, *args):
    try:
        solution = function(*args)
        return solution
    except Exception as error:
        error_message = "Exception: {}\n".format(error)
        sys.stderr.write(error_message)
        solution = None

    return solution
