#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)


# Test the function
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
length, first
