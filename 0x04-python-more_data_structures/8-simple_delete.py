#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for key in list(a_dictionary):
        if key == 'none':
            return a_dictionary
        else:
            del a_dictionary[key]
