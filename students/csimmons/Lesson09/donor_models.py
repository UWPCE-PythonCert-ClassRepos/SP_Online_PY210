#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom_oo.py assignment
# Donor classes 
# Created 1/17/2021 - csimmons


# single donor - name, donation record, # gifts
# avg gift. 
# Donor works directly with list of donations
# single thank you letter
class Donor(object):
       
    def __init__(self, name='', donations= []):
        self.name = name
        self.donations = donations

    def __str__(self):
        return f'Donor Name is: {self.name}'

    def __repr__(self):
        return f'Donor({self.name})'
        
    @property
    def total_donations():
        return sum(self.donations)

    @property
    def number_donations(self):
        return len(self.donations)
        
    @property
    def avg_donation():
        return sum(self.donations) / len(self.donations)

    def print_thankyou(self, name, donation):
        pass

# all donor objects - new donor, add donor, donor search, report generation
# DonorCollection does NOT works directly with list of 
# donations. GRoup reports belong here

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

    def add_donor(self, donor, donation):
        self.donors_db[donor] = Donor(donor,[donation])
        return self.donor_db

    def update_donor(self, donor, donation):
        self.donors_db[donor] = Donor(donor,[donation])
        return self.donor_db

    @property
    def donor_list(self):
        return list(self.donors_db)


    def __repr__(self):
        return "DonorCollection({})".format(self.donors_db)

    def donor_info_setter():
        pass

    def donor_info_getter():
        pass

    def find_donor(self):
        pass

    def update_donor(self):
        pass

    def donor_list(self):
        pass

    def donor_report(self):
        pass

    def batch_thankyou(self):
        pass