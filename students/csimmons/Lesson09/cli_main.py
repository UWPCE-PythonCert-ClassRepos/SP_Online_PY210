#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom_oo.py assignment
# CLI and Main program
# Created 1/17/2021 - csimmons


import pytest
from donor_models import *

def donordata():
    dc = DonorCollection()
    for name, donations in dc.donors_db.items():
        d = Donor(name, donations)
        print(name, donations, d.total_donations, d.number_donations, d.avg_donation)


def test_find_donor(name):
    dc = DonorCollection()
    '''
    d = Donor(name= 'Craig Simmons', donations= 75000)
    s = 'Mary Newcomer'
    if s in dc.donors_db.keys():
        print(s.donations, s.total_donations)
    else:
        print(s.donations)
    '''
    if name in dc.donors_db.keys():
        print(name + ' is in the database')
    else:
        return False

def initialize_donor_dict():
        dc = DonorCollection()
        for donor, donation in dc.donors_db.items():
            objname = Donor(donor, donation)
            print(objname)
        print(dc)

def initialize_donor_dict():
    dc = DonorCollection()
    for donor, donation in dc.donors_db.items():
        objname = Donor(donor, donation)
        dc = dc + objname
    return dc




if __name__ == '__main__':
    print('\nWelcome to the Mailroom Application!\n')
    #menu_select(text_dict.get('menu_prompt'), menu_dict)