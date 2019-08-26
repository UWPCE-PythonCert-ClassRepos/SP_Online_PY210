#!/usr/bin/env python

"""
Programming In Python - Lesson 6 Exercise 1: Unit Tests
Code Poet: Anthony McKeever
Start Date: 08/19/2019
End Date: 08/19/2019
"""

"""
When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


def walnut_party(walnuts, is_weekend):
    return walnuts >= 40 if is_weekend else walnuts in range(40, 61)    
