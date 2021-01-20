#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom_oo.py assignment
# Donor classes 
# Created 1/17/2021 - csimmons
from operator import itemgetter
class Donor(object):
       
    def __init__(self, name='', donations= []):
        self.name = name
        self.donations = donations

    def __str__(self):
        return f'Donor Name is: {self.name}'

    def __repr__(self):
        return f'Donor({self.name})'
        
    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def number_donations(self):
        return len(self.donations)
        
    @property
    def avg_donation(self):
        return sum(self.donations) / len(self.donations)


class DonorCollection(object):

    donors_db = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Ruotolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

    def __init_(self):
        self.donors_db = donors_db

    def __str__(self):
        return f'str: DonorCollection Object'

    def __repr__(self):
        return f'repr: DonorCollection Object'

    def find_donor(self, name):
        if name in self.donors_db.keys():
            return True
        else:
            return False
    
    def add_donor(self, donor, donations):
        donor = donor.title()
        new = Donor(donor, donations)
        self.donors_db.setdefault(new.name, []).append(new.donations)
        return self.donors_db

    def update_donor(self, donor, donations):
        new = Donor(donor, donations)
        self.donors_db.setdefault(new.name, []).append(new.donations)
        return self.donors_db

    def edit_donor(self, donor, donations):
        new = Donor(donor, donations)
        self.donors_db.setdefault(new.name, []).append(new.donations)
        return self.donors_db

    def create_report(self):
        self.all_info = []
        for donor, donation in self.donors_db.items():
            d = Donor(donor, donation)
            donor_info = [d.name, d.total_donations, d.number_donations, d.avg_donation]
            self.all_info.append(donor_info)
        self.all_info = sorted(self.all_info, key=itemgetter (1), reverse=True)
        return(self.all_info)

    @property
    def donor_list(self):
        return list(self.donors_db.keys())
