#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int_value = int(value)
        str_value = str(int_value)
        if str_value == str(value):
            print("{:d}".format(int_value))
            return True
        else:
            return False
    except:
        return False
