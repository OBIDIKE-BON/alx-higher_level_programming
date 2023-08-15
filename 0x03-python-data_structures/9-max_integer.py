#!/usr/bin/python3
def max_integer(my_list=[]):
    val = 0
    if len(my_list) < 1:
        return None
    for x in my_list:
        val = x if x > val else val
    return val
