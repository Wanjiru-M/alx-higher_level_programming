#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set1 = set_1 - set_2
    diff_set2 = set_2 - set_1
    return diff_set1.union(diff_set2)
