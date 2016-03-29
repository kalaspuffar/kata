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
    >>> roman_numbers("IV")
    4
    >>> roman_numbers("V")
    5
    >>> roman_numbers("VI")
    6
    """
    value = 0
    for n in list(nbr_str):
        next_value = 0
        if n == "I":
            next_value = 1
        elif n == "V":
            next_value = 5

        if next_value > value:
            value = next_value - value
        else:
            value += next_value
    print(value)
