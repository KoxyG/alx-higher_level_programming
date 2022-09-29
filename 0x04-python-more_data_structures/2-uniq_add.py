#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    """Using set data type to authomatically remove all the duplicated values"""
    for element in set(my_list):
        sum += element
        return sum
