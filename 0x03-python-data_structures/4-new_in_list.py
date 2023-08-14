#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    if 0 <= idx < len(copied_list):
        copied_list[idx] = element
    return copied_list


# Test the function
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

new_list, my_list
