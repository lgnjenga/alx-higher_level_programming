#!/usr/bin/python3

def multiply(n):
    return n * factor


def multiply_list_map(my_list=[], number=0):
    global factor
    factor = number
    return list(map(multiply, my_list))
