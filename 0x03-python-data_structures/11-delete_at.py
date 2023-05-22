#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        modified_list = my_list.copy()
        del modified_list[idx]
        return modified_list
