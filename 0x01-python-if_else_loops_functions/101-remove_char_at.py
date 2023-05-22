#!/usr/bin/python3
def remove_char_at(string, index):
    if index >= 0:
        result = string[:index] + string[index+1:]
    else:
        result = string
    return result
