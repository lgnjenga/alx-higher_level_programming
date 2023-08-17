#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    """
    if not a_dictionary or len(a_dictionary) == 0:
        return None

    return max(a_dictionary, key=a_dictionary.get)
