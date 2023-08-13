#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if __name__ == "main":
        if len(my_list) > 0:
            for i in my_list:
                print("{:d}".format(i))
