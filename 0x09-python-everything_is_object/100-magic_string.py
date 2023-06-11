#!/usr/bin/python3

def magic_string():
    if not hasattr(magic_string, "count"):
        magic_string.count = 1
    else:
        magic_string.count += 1
    
    string_list = []
    for _ in range(magic_string.count):
        string_list.append("BestSchool")
    
    return ", ".join(string_list)
