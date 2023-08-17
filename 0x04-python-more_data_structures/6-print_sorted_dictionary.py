#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = sorted(a_dictionary)
    for x in lst:
        print(f"{x}: {a_dictionary[x]}")
