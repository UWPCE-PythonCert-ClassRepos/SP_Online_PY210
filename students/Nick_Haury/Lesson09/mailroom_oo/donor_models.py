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

    email_template_string = ("Dear {},\n\n"
           "It is with incredible gratitude that we accept your wonderfully "
           "generous donation of ${:,.2f}.  Your "
           "contribution will truly make a difference in the path forward "
           "towards funding our common goal."
           "\n\nEver Greatefully Yours,\n\n"
           "X" + ("_" * 20) + "\n")
    
    def __init__(self, donor_name, donations = []):
        self._name = donor_name
        self._donations = donations

    @property
    def name(self):
        return self._name
    
    @property
    def donations(self):
        return self._donations

    def email_text(self, donation_index):
        try:
            return self.email_template_string.format(
                self.name, self.donations[donation_index])
        except IndexError:
            return None


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

    @property
    def names(self):
        return list(self.donors.keys())

    def report(self):
        pass

    def add_donation(self, donor_name, donation):
        if donor_name in self.names:
            self.donors[donor_name].add_donation(donation)
        else:
            self.donors[donor_name] = Donor(donor_name, [donation])


if __name__ == "__main__":
    pass