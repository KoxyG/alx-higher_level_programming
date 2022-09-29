#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """creating a function to search before replacing."""
    def find_search(element):
        return element if element != search else replace
    return list(map(find_search, my_list))
