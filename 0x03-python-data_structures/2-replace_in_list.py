#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    le = len(my_list)
    if ((idx >= 0) and (le > 0)) and ((idx <= le - 1)):
        my_list[idx] = element
        return my_list
    return my_list
