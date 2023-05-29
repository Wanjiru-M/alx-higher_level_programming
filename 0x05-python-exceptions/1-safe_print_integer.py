#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if str(value).isnumeric():
            print("{:d}".format(int(value)))
            return True
        else:
            return False
    except:
        return False
