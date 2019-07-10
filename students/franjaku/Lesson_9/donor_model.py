#!/usr/bin/env python
"""
Donor models contains the Donor and DonorColletion classes.
"""
from functools import total_ordering

# Donor
@total_ordering
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
        self._name = name
        self._donations = []

    def __str__(self):
        return "Donor: {}".format(self.name)

    def __repr__(self):
        return "Donor({})".format(self.name)

    def __lt__(self, other):
        return (self.total_donated < other.total_donated)

    def __eq__(self, other):
        return (self.total_donated == other.total_donated)

    def add_donation(self, donation):
        if type(donation) == float or int:
            if donation > 0:
                self._donations.append(donation)
            else:
                print('Donation must be > 0')
                raise ValueError
        else:
            print('Donation must by integer or float')
            raise TypeError

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def total_donated(self):
        return sum(self.donations)

    @property
    def average_donation(self):
        return self.total_donated / self.num_donations


# Collection of donors
class DonorColletion(object):
    pass
