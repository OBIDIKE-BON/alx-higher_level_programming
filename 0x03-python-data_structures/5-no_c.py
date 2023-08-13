#!/usr/bin/python3
def no_c(my_string):
    le = len(my_string)
    if le > 0:
        new_str = ""
        for i in range(le):
            if (my_string[i] != "c") and my_string[i] != "C":
                new_str += my_string[i]
        return new_str
    return my_string
