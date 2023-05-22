#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return_count = len(sentence)
        default_value = None
        return return_count, default_value
    else:
        return_count = len(sentence)
        first_char = sentence[0]
        return return_count, first_char
