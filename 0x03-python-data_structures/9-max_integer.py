#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    max_val = None
    for num in my_list:
        if max_val is None or num > max_val:
            max_val = num
    return max_val


# Test the function
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
max_value
