#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        x = 0
        for i in range(x):
            print(f"{my_list[i]}", end=")
            x += 1
            return x
    except IndexError:
        break
    print()
    return x
