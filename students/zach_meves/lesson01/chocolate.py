"""
chocolate.py
Zachary Meves
Python 210
Lesson 01

Solves CodingBat Logic-2, make_chocolate problem.
"""


def make_chocolate(small, big, goal):
    """Compute number of small bars required to meet the set goal, given the
   number of small and large bars available.

    Parameters
    ----------
    small : int
        Number of small bars available (1 kg each)
    big : int
        Number of large bars available (5 kg each)
    goal : int
        Total amount requested

    Returns
    -------
    int
        Number of small bars that will be used, or -1 if it cannot be done"""
    sz_small, sz_large = 1, 5

    # Number of large bars that are used
    n_large = min(int(goal / sz_large), big)
    tot_large = n_large * sz_large

    # Amount to use small bars for
    remaining = goal - tot_large

    if remaining > small:
        return -1
    else:
        return remaining
