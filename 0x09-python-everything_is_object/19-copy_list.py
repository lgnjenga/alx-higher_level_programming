#!/usr/bin/python3
def copy_list(a):
    """Copy a list using a loop and return the new list.

    Args:
        a (list): The list to be copied.

    Returns:
        list: A new list with the same elements as the input list.
    """
    new_list = []
    for item in a:
        new_list.append(item)
    return new_list
