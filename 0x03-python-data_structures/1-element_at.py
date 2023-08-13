#!/usr/bin/python3
def element_at(my_list, idx):
    le = len(my_list)
    if idx >= 0 and le > 0 and le - 1 <= idx:
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
