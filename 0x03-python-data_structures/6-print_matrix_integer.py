#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row_list in matrix:
        for index, element in enumerate(row_list):
            end_char = " " if index < len(row_list) - 1 else ""
            print("{:d}".format(element), end=end_char)
        print()
