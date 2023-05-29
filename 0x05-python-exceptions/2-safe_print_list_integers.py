#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    def generator():
        nonlocal i
        while i < x:
            try:
                yield my_list[i]
                i += 1
            except IndexError:
                break
    for value in generator():
        if isinstance(value, int):
            print("{:d}".format(value), end=" ")
            count += 1
    print()
    return count
