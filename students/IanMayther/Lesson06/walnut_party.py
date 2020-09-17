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
    if walnuts <= 40 and is_weekend == False:
        success = False
    elif walnuts > 40 and walnuts <= 60 and is_weekend == False:
        success = True
    elif walnuts >= 40 and is_weekend == True:
        success = True
    
    return success
