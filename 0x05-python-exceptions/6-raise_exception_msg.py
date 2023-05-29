#!/usr/bin/python3
def raise_exception_msg(message=""):
    eval("undefined_variable", {'__builtins__': None}, {'message': message})

