#!/usr/bin/env python3

'''
Classes for the object oriented version of the mailroom program.

Defines the Donor and DonorCollection Classes.  Donor tracks a donor's name,
along with a list of their donations.  DonorCollection collects the donors into
a dictionary.
'''

class Donor:
    """
    Donor keeps track of a donor's name and a list of previous donation amounts
    they have donated in the past.

    Parameters
    ----------
    donor_name : str
        Name of donor
    donations   :   list
        list of ints or floats that are donations made by donor
    """
    
    def __init__(self, donor_name, donations = []):
        self._name = donor_name.lower()
        self._donations = donations

    @property
    def name(self):
        return self._name
    
    @property
    def donations(self):
        return self._donations

    def add_donation(self, donation_amount):
        '''add a donation to the donor's list,
        must be positive type int or float
        '''
        if isinstance(donation_amount, (int, float)):
            if donation_amount > 0:
                self.donations.append(donation_amount)
            else:
                raise ValueError("donation must be a positive value")
        else:
            raise TypeError('donation must be of type int or float')

    def __str__(self):
        return f'Donor named {self._name} with {len(self.donations)} donations.'

    def __repr__(self):
        return f'Donor("{self._name}", {self.donations})'


class DonorCollection:

    def __init__(self, donor_dict_input = {}):
        if isinstance(donor_dict_input, dict):
            self.donors = donor_dict_input
        else:
            raise TypeError("donor_dict_input must be a dictionary")

    def add_donor(self, donor):
        if isinstance(donor, Donor):
            self.donors[donor.name] = donor
        else:
            raise TypeError("donor must be of Class Donor")

    def get_names(self):
        return list(self.donors.keys())

    def report(self):
        pass


if __name__ == "__main__":
    pass