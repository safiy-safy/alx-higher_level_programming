#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Args:
        sentence: a string argument

    Returns:
        a tuple with the length of a string and its first character
    """

    str_len, first_char = len(sentence), sentence[0]
    return (str_len, first_char)
def multiple_returns(sentence):
    if len(sentence) == 0:
        my_tuple = (0, None)
    else:
        my_tuple = (len(sentence), sentence[:1])
    return(my_tuple)
