#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float, optional): The second integer (default is 98).

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b


if __name__ == "__main__":
    add_integer = __import__('0-add_integer').add_integer

    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
