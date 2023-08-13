#!/usr/bin/python3
def element_at(my_list, idx):
    le = len(my_list)
    if idx >= 0 and le > 0 and le - 1 <= idx:
        print("{:d}".format(my_list[idx]))
