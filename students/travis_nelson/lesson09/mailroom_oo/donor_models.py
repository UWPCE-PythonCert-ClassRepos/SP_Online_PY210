import sys

class Donor(object):

    """
    Class responsible for donor data encapsulation

    This class will hold all the information about a single donor,
    and have attributes, properties, and methods to provide access
    to the donor-specific information that is needed. Any code that
    only accesses information about a single donor should be part of
    this class.
    """

    def __init__(self, name="Anonymous", initial_donation=0):
        """New donor instance may be created with a name and/or a donation amount.
        The donation may be a single value, or a list of donations (as you would
        if you were backfilling an entry
        """
        # this allows for anonymous donation handling
        if type(name) is not str and initial_donation == 0:
            self.donations = [name]
            self.name = "Anonymous"
        else:
            self.name = name
            if type(initial_donation) is list:
                self.donations = [i for i in initial_donation]
            else:
                self.donations = [initial_donation]

    def __repr__(self):
        return f"Donor('{self.name}', {self.donations})"

    def add_donation(self, donation=0):
        self.donations.append(donation)

    @property
    def sum_donations(self):
        return sum(self.donations)

    @property
    def number_donations(self):
        return len(self.donations)

    @property
    def average_donation(self):
        return round(self.sum_donations / self.number_donations, 2)


class Donor_Collection():
    pass