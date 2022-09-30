#!/usr/bin/python3
def best_score(a_dictionary):
    """using max built-in & get method to find the maxinum score"""
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
