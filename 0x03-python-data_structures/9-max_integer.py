#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value

my_list = [30, 90, -13, 4, 6]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
