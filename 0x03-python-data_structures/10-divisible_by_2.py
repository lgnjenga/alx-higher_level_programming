#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [True if num % 2 == 0 else False for num in my_list]


# Test the function
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

list_result
