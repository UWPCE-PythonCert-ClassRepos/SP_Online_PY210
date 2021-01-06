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
    if walnuts < 40 or walnuts == 61:
        is_weekend = False
    else:
        is_weekend = True
    return is_weekend


"""
assert walnut_party(30, True) is False
assert walnut_party(39, True) is False
assert walnut_party(30, False) is False
assert walnut_party(39, False) is False
assert walnut_party(61, False) is False





assert walnut_party(40, False) is True
assert walnut_party(50, False) is True
assert walnut_party(60, False) is True
assert walnut_party(40, True) is True
assert walnut_party(50, True) is True
assert walnut_party(70, True) is True








"""