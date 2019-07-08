#!/usr/bin/env python
"""
Donor models contains the Donor and DonorColletion classes.
"""


# Donor
class Donor(object):
    """
    Create a new donor object (expand).

    Contains all the information for a single donor, including all methods
    necessary to work on that donor. Uses total_ordering to be able to sort.

    Donor Properties
    - donor.name: string with donor name
        - can't be change after init
    - donor.donations: list containing donations
        - can append to it
    - total dontation amount
    - total # of donations
    - average donation amount

    Donor Methods
    - add a donation to donors history
    - compute total donation amount by a donor
    - compute total number of donations by a donor
    - compute average donation amount
    """
    def __init__(self, name):
        """
        Initialize with only a name.
        Because of the error checking required for adding a donation I am
        choosing to not add a donation amount in __init__.
        """
        pass


# Collection of donors
class DonorColletion(object):
    pass