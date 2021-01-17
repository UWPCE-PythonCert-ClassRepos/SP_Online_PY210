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
       
    def __init__(self, name='', donation= []):
        self.name = name
        self.donation = donation
        


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

    def __init__(self, name='', donation= 0, data='donors_db'):
        self.name = name
        self.donation = donation
        self.donors_db = donors_db