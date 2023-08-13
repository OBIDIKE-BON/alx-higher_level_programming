#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    le = len(my_list)
    if ((idx >= 0) and (le > 0)) and ((idx <= le - 1)):
        for i in range(len(my_list) - 1, -1, -1):
            print(my_list[i])
