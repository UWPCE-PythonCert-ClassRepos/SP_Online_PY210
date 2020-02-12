#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


def walnut_party(walnuts: int, is_weekend: bool):
    # Test inputs
    try:
        complex(walnuts)
        if not isinstance(is_weekend, bool):
            raise TypeError("is_weekend is not boolean")
    except ValueError:
        raise ValueError("Walnuts is not a number")

    # function logic
    answer = False
    if 40 <= walnuts <= 60:
        answer = True
    elif is_weekend and walnuts > 60:
        answer = True

    return answer
