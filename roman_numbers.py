"""
This kata will try to parse roman numbers in small increments using python
and doctest.
"""
def roman_numbers(nbr_str):
    """
    Examples:
    >>> roman_numbers("I")
    1
    >>> roman_numbers("II")
    2
    >>> roman_numbers("V")
    5
    >>> roman_numbers("VI")
    6
    """
    val = 0
    for n in list(nbr_str):
        if n == "I":
            val += 1
        elif n == "V":
            val += 5
    print(val)
