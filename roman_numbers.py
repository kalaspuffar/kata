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
    >>> roman_numbers("IX")
    9
    >>> roman_numbers("X")
    10
    >>> roman_numbers("XV")
    15
    >>> roman_numbers("L")
    50
    >>> roman_numbers("C")
    100
    >>> roman_numbers("D")
    500
    >>> roman_numbers("M")
    1000
    >>> roman_numbers("CIX")
    109
    """
    value = 0
    previous_value = 0
    roman_numbers = ["I", "V", "X", "L", "C", "D", "M"]
    decimal_numbers = [1, 5, 10, 50, 100, 500, 1000]
    for n in list(nbr_str):
        next_value = 0
        for idx, val in enumerate(roman_numbers):
            if n == val:
                next_value = decimal_numbers[idx]

        if next_value > previous_value:
            value += next_value - previous_value * 2 
        else:
            value += next_value
        previous_value = next_value
    print(value)
