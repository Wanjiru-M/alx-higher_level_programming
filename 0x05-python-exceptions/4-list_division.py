#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    sol = []
    for i in range(list_length):
        try:
            sol.append(my_list_1[i] / my_list_2[i])
        except (IndexError, TypeError):
            if i >= min(len(my_list_1), len(my_list_2)):
                print("out of range")
            else:
                print("wrong type")
            sol.append(0)
        except ZeroDivisionError:
            sol.append(0)
    return sol
