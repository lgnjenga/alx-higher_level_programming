def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


# Test the function
my_list = [1, 2, 3, 4, 5]
idx = 3
element_at(my_list, idx)
