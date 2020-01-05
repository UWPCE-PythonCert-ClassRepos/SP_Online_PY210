#!/usr/bin/env python3

"""
Mail_room_oo.py
By David Baylor on 12/31/19
uses python 3

Automates writing an email to thank donors for their donations.
"""

import sys
from operator import itemgetter

class Donor():
    """holds the data for a single donnor"""
    def __init__(self, name, total_donated, donations=1):
        """initializes Donor with total_donated, donations, and name"""
        self.total_donated = total_donated
        self.donations = donations
        self.name = name
    
    def __repr__(self):
        """returns '<self.name, total donated: self.total_donated>' """
        return f"<{self.name}, total donated: {self.total_donated}>"

    def __lt__(self, other):
        """redefines 'less than' for sorting"""
        return (self.total_donated < other.total_donated)

    @property
    def average_donation(self):
        """gets average donation"""
        return self.total_donated/self.donations

class DonorCollection():
    """holds all the donor objects and contains methods to manipulate donor data"""
    def __init__(self):
        """initializes DonorCollection with a donor_dict"""
        self.donor_dict = {}
    
    def get_donor(self, name):
        """gets donor from donor_dict"""
        return self.donor_dict[name]

    def sort_lst(self):
        """sorts the values of donor_dict from greatest to smallest"""
        lst = list(self.donor_dict.values())
        lst.sort(reverse=True)
        return lst

    def add_donation(self, name, donation, donations=1):
        """
        adds a donation if the donor is in donor_dict
        otherwise adds a new donor
        """
        if name in self.donor_dict:
            self.donor_dict[name].total_donated += donation
            self.donor_dict[name].donations += 1
        else:
            donor = Donor(name, donation, donations)
            self.donor_dict[name] = donor

    def check_donor_in_db(self, name):
        """checks if the donor is in the data bace"""
        if name in self.donor_dict:
            return True
        else:
            return False
        
