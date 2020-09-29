#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


def walnut_party(walnuts, is_weekend):
    if is_weekend and walnuts >= 40:
        return True
    elif not is_weekend and 40 <= walnuts and 60 >= walnuts:
        return True
    else:
        return False
