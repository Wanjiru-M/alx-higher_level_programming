#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    return None
def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
