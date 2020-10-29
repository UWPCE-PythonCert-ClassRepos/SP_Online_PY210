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

    def add(self, input):
        if type(input) is not Donor:
            raise TypeError('Input must be a single Donor object.')
        self.donor_list.append(input)

    def new(self, first, last, donations):
        return 200

#    @property
#    def alphabetical(self):
#        '''
#        Generates an alphabetical list of donors by name.
#        '''
#        return sorted(
