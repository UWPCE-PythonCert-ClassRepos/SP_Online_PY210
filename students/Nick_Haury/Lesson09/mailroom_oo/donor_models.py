#!/usr/bin/env python3

'''
Classes for the object oriented version of the mailroom program.
'''

class Donor:
    
    def __init__(self, donor_name, donations = []):
        self._donor_name = donor_name
        self._donations = donations

    @property
    def donor_name(self):
        return self._donor_name
    
    @property
    def donations(self):
        return self._donations
    

class DonorCollection:

    def __init__(self, donor = None):
        self.donor_dict["donor.name"]

    pass

if __name__ == "__main__":
    pass