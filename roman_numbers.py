"""
This kata will try to parse roman numbers in small increments using python
and doctest.
"""
def roman_numbers(nbr_str):
    """
    Examples:
    >>> roman_numbers("I")
    1
    >>> roman_numbers("V")
    5
    """
    if nbr_str == "I":
        print(1)
    elif nbr_str == "V":
        print(5)
