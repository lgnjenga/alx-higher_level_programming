#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Return a new list replacing all occurrences of 'search' by 'replace'.
    """
    # Use list comprehension to generate the new list
    return [x if x != search else replace for x in my_list]
