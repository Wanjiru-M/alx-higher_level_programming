#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            printed_elements += 1
            continue
    print()
    return printed_elements
