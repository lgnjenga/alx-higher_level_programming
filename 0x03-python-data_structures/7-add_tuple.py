#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure the tuples have at least 2 elements. If not, pad with zeros.
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Create the new tuple by adding the first two elements of each tuple.
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple


# Test the function
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
test1 = new_tuple

test2 = add_tuple(tuple_a, (1, ))
test3 = add_tuple(tuple_a, ())

test1, test2, test3
