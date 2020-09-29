#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 1/20/2020
# donor_models.py


import os


class Donor(object):

    def __init__(self, donor_name, donations):
        '''Donor class input: Full Name, [total_donations, num_donations].'''
        self._name = self.check_name(donor_name)
        self._donations = self.check_donation(donations)

    @staticmethod
    def check_name(name):
        '''Checks the name entry for a Full Name (First and Last).'''
        try:
            name.split()[1]
            name = name.title()
            return name.title()
        except TypeError:
            raise ('Name must contain a first and last name')

    @staticmethod
    def check_donation(donation):
        '''Checks the donation data for two positive values, > 0 [float, int].'''
        if (donation[0] > 0 and donation[1] > 0):
            donation[1] = int(donation[1])
            return donation
        else:
            raise AttributeError('Donations must be positive values, > 0 [float, int]')

    @property
    def name(self):
        '''Returns donor name'''
        return self._name

    @name.setter
    def name(self, value):
        '''Blocks setting name of the donor.'''
        raise AttributeError('Name cannot be set')

    @property
    def donations(self):
        '''Returns the donation data.'''
        return self._donations

    @donations.setter
    def donations(self, donation):
        '''Blocks setting donations for the donor.'''
        raise AttributeError('Donations cannot be set')

    @property
    def total_donations(self):
        '''Returns total donation.'''
        return self._donations[0]

    @staticmethod
    def add_total_donations(self, donation):
        '''Adds the new donation value to the current total donations.'''
        self._donations[0] = self.total_donations + self.check_donation_value(donation)

    @staticmethod
    def check_donation_value(donation):
        '''Checks if the donation is greater than zero.'''
        if donation > 0:
            return donation
        else:
            raise AttributeError('Donations must be positive values, greater than zero')

    @property
    def num_donations(self):
        '''Returns number donations.'''
        return self._donations[1]

    @staticmethod
    def add_num_donations(self):
        '''Adds one to the number of donations.'''
        self._donations[1] = self.num_donations + 1

    @property
    def avg_donations(self):
        '''Calculates the average donations of the donor.'''
        return self.total_donations / self.num_donations

    @avg_donations.setter
    def avg_donations(self, value):
        '''Blocks setting average donations for the donor.'''
        raise AttributeError('Average donation cannot be set')

    def new_donation(self, donation):
        '''Adds a new donation to the donors donation data.'''
        self.add_total_donations(self, donation)
        self.add_num_donations(self)

    def save_donor_file(self, letter):
        '''Saves a letter for the donor to file.'''
        first_name = self.name.split()[0]
        last_name = self.name.split()[1].strip(',')
        file_path = os.path.join("./{}_{}.txt".format(first_name, last_name))
        with open(file_path, 'w+') as new_file:
            new_file.write(letter)


def sort_key(values):
    '''Sorts the DonorCollection by historical value.'''
    return values[1]


class DonorCollection(Donor):
    '''Collection of donors.'''

    def __init__(self, *args):
        self._donors = {donor.name: donor for donor in args}

    @property
    def donors(self):
        '''Returns a collection of donors.'''
        return self._donors

    def is_donor_present(self, donor_name):
        '''Checks if the donor is present in the collection.'''
        if self.donors.get(donor_name):
            return True
        else:
            return False

    def get_donors_names(self):
        '''Returns collection names.'''
        return self.donors.keys()

    def add_donation(self, donor_name, donation):
        '''Appends donor donation data.'''
        if self.donors.get(donor_name):
            self.donors[donor_name].new_donation(donation)
        else:
            self.donors[donor_name] = Donor(donor_name, [donation, 1])

    def get_report(self):
        '''Gets a collection of donors, sorted by total donation amount.'''
        report = []
        for donor, data in self.donors.items():
            new_data = (donor, data.total_donations, data.num_donations,
                        data.avg_donations)
            report.append(new_data)
        report.sort(key=sort_key, reverse=True)
        return report
