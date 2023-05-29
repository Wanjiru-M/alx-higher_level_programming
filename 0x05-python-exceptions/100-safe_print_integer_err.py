#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("%d" % int(value))
        return True
    except Exception as e:
        print("Exception: %s" % e, file=sys.stderr)
        return False
