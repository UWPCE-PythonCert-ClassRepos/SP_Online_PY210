#!/usr/bin/env python3
import statistics as st

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
    name            :   str
        Name of donor in lowercase
    display_name    :   str
        Name of donor with original capitalization
    donations       :   list
        list of ints or floats that are donations made by donor
    """

    email_template_string = ("Dear {},\n\n"
           "It is with incredible gratitude that we accept your wonderfully "
           "generous donation of ${:,.2f}.  Your "
           "contribution will truly make a difference in the path forward "
           "towards funding our common goal."
           "\n\nEver Greatefully Yours,\n\n"
           "X" + ("_" * 20) + "\n")
    
    def __init__(self, donor_name, donations = None):
        if donations == None:
            self._donations = []
        else:
            self._donations = donations
        self._name = donor_name.lower()
        self._display_name = donor_name

    @property
    def name(self):
        return self._name

    @property
    def display_name(self):
        return self._display_name
    
    @property
    def donations(self):
        return self._donations

    def email_text(self, donation_index):
        try:
            return self.email_template_string.format(
                self.display_name, self.donations[donation_index])
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

    def __lt__(self, other):
        '''sorts by sum of donations, then alphabetical by Donor name'''
        return (sum(self.donations), self.name) < (sum(other.donations), other.name)


class DonorCollection:

    def __init__(self, donor_dict_input = {}):
        if isinstance(donor_dict_input, dict):
            self.donors = donor_dict_input
        else:
            raise TypeError("donor_dict_input must be a dictionary"
                            "of form {'donor name':Donor()'}")

    def add_donor(self, donor):
        if isinstance(donor, Donor):
            self.donors[donor.name] = donor
        else:
            raise TypeError("donor must be of Class Donor")

    @property
    def names(self):
        return list(self.donors.keys())

    @property
    def display_names(self):
        return [donor.display_name for donor in self.donors.values()]

    def report(self):
        report_list = ["\nDonor Name" + " "*15 + "|  Total Given  "
                         "| Num Gifts |   Average Gift\n"]
        for donor in sorted(self.donors.values(), reverse=True):
            report_list.append(f"{donor.display_name:26}"
                               f"${sum(donor.donations):14,.2f}"
                               f"{len(donor.donations):11}  "
                               f"${st.mean(donor.donations):16,.2f}\n")
        return report_list

    def add_donation(self, donor_name, donation):
        if donor_name.lower() in self.names:
            # check to see if different capitalization is being used
            self.donors[donor_name.lower()].add_donation(donation)
        else:
            self.donors[donor_name.lower()] = Donor(donor_name, [donation])


if __name__ == "__main__":
    pass