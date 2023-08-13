#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    le = len(my_list)
    if ((idx >= 0) and (le > 0)) and ((idx <= le - 1)):
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    return my_list
