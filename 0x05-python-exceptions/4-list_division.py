#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divided_list = []
    for index in range(list_length):
        try:
            numerator = my_list_1[index]
            denominator = my_list_2[index]
            result = numerator / denominator
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            divided_list.append(result)
    return divided_list
