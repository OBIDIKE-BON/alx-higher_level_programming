#!/usr/bin/python3
def element_at(my_list, idx):
    le = len(my_list)
    if ((idx >= 0) and (le > 0)) and ((idx <= le - 1)):
        return my_list[idx]
