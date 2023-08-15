#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list


# Test the function
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)

new_list, my_list
