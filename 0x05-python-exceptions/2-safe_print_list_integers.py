#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer_count = 0
    for index in range(x):
        try:
            value = my_list[index]
            print("{:d}".format(value), end="")
        except (ValueError, TypeError):
            pass
        else:
            integer_count += 1
    print()
    return integer_count
