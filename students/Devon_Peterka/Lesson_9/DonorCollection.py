#!/usr/bin/env python 3

from Donor import Donor

class DonorCollection():
    def __init__(self, donors=None):
        # Make user input into a list if not already.  If a donor
        # object, initialize a list containing it.  If None, initialize
        # an empty list.  Otherwise accept as-is - for now...
        if type(donors) is Donor:
            donors = [donors]
        self.donor_list = [] if donors is None else donors

        # Check for valid input (i.e. - either empty list or list of
        # Donor objects only.  Raise exception if not.
        errormessage = 'DonorCollection object may only be initialized empty or with a list of Donor-type objects'
        if type(self.donor_list) is not list:
            raise TypeError (errormessage)
        for i in range(len(self.donor_list)):
            if type(self.donor_list[i]) is not Donor:
                raise TypeError (errormessage)

    def __repr__(self):
        return str(self.donor_list)
    
    def __str__(self):
        return str(self.donor_list)
    
    def __getitem__(self, index):
        return self.donor_list[index]

    def add(self, input):
        if type(input) is not Donor:
            raise TypeError('Input must be a single Donor object.')
        self.donor_list.append(input)

    def new(self, first, last, donations):
        new_donor = Donor(first, last, [donations])
        self.add(new_donor)

    @property
    def list(self):
        '''
        Generates an alphabetical list of donors by name.
        '''
        return sorted(self.donor_list,key=Donor.sort_by_name)
    
    @property
    def list_by_donation(self):
        '''
        Generates a list of donors sorted by total donation in
        descending order.
        '''
        return sorted(self.donor_list, key=Donor.sort_by_donations, reverse=True)
    
    @staticmethod
    def report(donors):
        header = 'Donor Name          |  Total Given   | Gifts |  Average Gift  |\n'
        linebreak = ('-' * 20 + '|' + '-' * 16 + '|' + '-' * 7 + '|' + '-' * 16 + '|\n')
        report_output = header + linebreak
        for i in range(len(donors)):
            donor = donors[i].full_name
            donation = donors[i].total_donation
            gifts = len(donors[i].donations)
            avg = 0 if gifts == 0 else donation/gifts
            report_output += f'{donor:.<20}| ${donation:>13,.2f} | {gifts:^5d} | ${avg:13,.2f} |\n'
        report_output += linebreak
        return report_output
