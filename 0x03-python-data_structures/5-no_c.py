#!/usr/bin/env python3
def no_c(my_string):
    return ''.join([char for char in my_string if char not in ['c', 'C']])


# Test the function
test_strings = ["Best School", "Chicago", "C is fun!"]
results = [no_c(s) for s in test_strings]

results
