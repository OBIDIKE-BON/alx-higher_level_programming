#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = len(sys.argv) - 1
    if ac == 0:
        sufix = "arguments."
    elif ac == 1:
        sufix = "argument:"
    else:
        sufix = "arguments:"
    print("{} {}".format(ac, sufix))
    for index, arg in enumerate(sys.argv, start=0):
        if index != 0:
            print("{}: {}".format(index, arg))
