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
    >>> roman_numbers("CIIX")
    108
    >>> roman_numbers("CIX")
    109
    >>> roman_numbers("D")
    500
    >>> roman_numbers("M")
    1000
    >>> roman_numbers("MCMXCIX")
    1999
    >>> roman_numbers("MCMXCVIIII")
    1999
    >>> roman_numbers("MCMLXXXXIX")
    1999
    >>> roman_numbers("MCMLXXXXVIIII")
    1999
    >>> roman_numbers("MDCCCCXCIX")
    1999
    >>> roman_numbers("MDCCCCXCVIIII")
    1999
    >>> roman_numbers("MDCCCCLXXXXIX")
    1999
    >>> roman_numbers("MDCCCCLXXXXVIIII")
    1999
    >>> roman_numbers("IIIII")
    NaN
    >>> roman_numbers("LIIIIIX")
    NaN
    >>> roman_numbers("MVV")
    NaN
    >>> roman_numbers("IC")
    NaN
    >>> roman_numbers("MIC")
    NaN
    """
    value = 0
    previous_roman_value = ""
    previous_decimal_value = 0
    roman_numbers = ["I", "V", "X", "L", "C", "D", "M"]
    decimal_numbers = [1, 5, 10, 50, 100, 500, 1000]
    failstate = False
    for n in list(nbr_str):
        next_value = 0
        current_idx = -1;
        for idx, val in enumerate(roman_numbers):
            if n == val:
                next_value = decimal_numbers[idx]
                current_idx = idx

        if not failstate and previous_decimal_value > 0 and next_value > previous_decimal_value * 10:
            print("NaN")
            failstate = True

        if next_value > previous_decimal_value:
            value += next_value - previous_decimal_value * 2 
        else:
            value += next_value

        if previous_roman_value == n:
            previous_decimal_value += next_value
        else:
            previous_decimal_value = next_value
        previous_roman_value = n

        if not failstate and current_idx < 6 and previous_decimal_value >= decimal_numbers[current_idx+1]:
            print("NaN")
            failstate = True
                        

    if not failstate:
        print(value)
