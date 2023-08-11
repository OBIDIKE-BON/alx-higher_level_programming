#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = len(sys.argv) - 1
    print("{} {}:".format(ac, ("argument" if ac == 1 else "arguments")))
    for index, arg in enumerate(sys.argv, start=0):
        if index != 0:
            print("{}: {}".format(index, arg))
