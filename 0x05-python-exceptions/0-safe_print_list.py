#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        x = 0
        for i in range(x):
            print(my_list[i])
            x += 1
            return x
    except IndexError:
        print("")
        return a
