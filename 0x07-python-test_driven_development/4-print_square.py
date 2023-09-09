#!/usr/bin/python3
def print_square(size):
    """
    Print a square of a specified size using the character #.

    :param size: The size (length) of the square.
    :type size: int
    :raises TypeError: If size is not an integer
     or if it's a float less than 0.
    :raises ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    # Test cases
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
