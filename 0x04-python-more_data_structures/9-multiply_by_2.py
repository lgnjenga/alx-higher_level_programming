def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.
    """
    # Use dictionary comprehension to create a new dictionary
    return {key: value * 2 for key, value in a_dictionary.items()}
