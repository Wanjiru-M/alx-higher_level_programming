#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    digit = 0
    try:
        for i in range(x):
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                digit += 1
            elif isinstance(element, str) and element.isdigit():
                print("{:d}".format(int(element)), end="")
                digit += 1
        print()
    except (IndexError, TypeError):
        pass
    return digit
