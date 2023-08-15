#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    val = my_list[0]
    for x in my_list:
        val = x if x > val else val
    return val
