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
    greater_than_39 = walnuts > 39
    less_than_61 = walnuts < 61
    if (not is_weekend) and greater_than_39 and less_than_61:
        return True
    if is_weekend  and greater_than_39:
        return True
    return False
