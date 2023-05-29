#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except (ValueError, TypeError) as error:
        error_message = "Exception: {}".format(error)
        print(error_message, file=sys.stderr)
        return False
