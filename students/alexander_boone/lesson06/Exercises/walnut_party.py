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
    """Return True if the squirrel party is successful. If the squirrel party
    is unsuccessful, return false.
    """
    if is_weekend:
        if walnuts >= 40:
            return True
        return False
    else:
        if 40 <= walnuts <= 60:
            return True
        return False
    pass
