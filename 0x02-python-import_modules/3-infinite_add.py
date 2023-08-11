#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    total = 0
    for index, arg in enumerate(sys.argv, start=0):
        if index != 0:
            total += int(sys.argv[index])
    print("{}".format(total))
