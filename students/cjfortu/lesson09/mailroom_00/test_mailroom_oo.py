#!/usr/bin/env python

"""
donor_models test suite.
"""

import io
import pytest
from io import StringIO
from donor_models import *


def test_initiate_donor():
    bobevans = Donor('Bob Evans', 1.1, 2.2)
    assert bobevans.name == 'Bob Evans'
    assert bobevans.donations == [1.1, 2.2]
    
def test_add_donations():
    bobevans = Donor('Bob Evans', 1.1, 2.2)
    bobevans.add_donations([30, 40, 50])
    assert bobevans.donations == [1.1, 2.2, 30, 40, 50]
    assert bobevans.new_donations == [30, 40, 50]
    bobevans.add_donations([0.6, 0.7, 800])
    assert bobevans.donations == [1.1, 2.2, 30, 40, 50, 0.6, 0.7, 800]
    assert bobevans.new_donations == [0.6, 0.7, 800]
    
def test_number_donations():
    jimmyjohns = Donor('Jimmy Johns', 3.3, 4.4, 5.5)
    assert jimmyjohns.number_donations == 3
    
def test_lifetime_donations_sum():
    jimmyjohns = Donor('Jimmy Johns', 3.3, 4.4, 5.5)
    assert jimmyjohns.lifetime_donations_sum == 13.2
    
def test_average_donations():
    jimmyjohns = Donor('Jimmy Johns', 3.3, 4.4, 5.5)
    assert jimmyjohns.average_donations == 13.2/3
    jimmyjohns.add_donations([30, 40, 50])
    assert jimmyjohns.average_donations == 133.2/6
    
def test_compose_letter():
    bobevans = Donor('Bob Evans', 1.1, 2.2)
    bobevans.add_donations([30, 40, 50])
    assert bobevans.compose_letter == """\n\nHi Bob Evans,\n\nThank you for your total donation of $120.00.
\n\nVR\n\nThe Mailroom\n(555) 555-5555"""
    jimmyjohns = Donor('Jimmy Johns', 3.3, 4.4, 5.5)
    assert jimmyjohns.compose_letter == """\n\nHi Jimmy Johns,\n\nThank you for your total donation of $13.20.
\n\nVR\n\nThe Mailroom\n(555) 555-5555"""

def test_build_collection():
    donors_A = DonorCollection(**{'Bob Evans': [1.1, 2.2], 'Billy': [30.3,0.4, 5000000.5]})
    assert donors_A.data['Bob Evans'].donations == [1.1, 2.2]
    
def test_add_donor():  # verified effect on other methods here
    donors_A = DonorCollection(**{'Bob Evans': [1.1, 2.2], 'Billy': [30.3,0.4, 5000000.5]})
    donors_A.add_donor('Jersey Mikes', 6, 7.00)
    donors_A.add_donor('New Guy')
    assert donors_A.data['Bob Evans'].name == 'Bob Evans'
    assert donors_A.data['Jersey Mikes'].donations == [6, 7.00]
    assert donors_A.data['Jersey Mikes'].average_donations == 6.5
    assert donors_A.data['New Guy'].name == 'New Guy'
    
def test_names():
    donors_A = DonorCollection(**{'Bob': [17.56], 'Billy': [500.00, 1000.00], 'Joe Schmoe': [2.00, 0.03, 45.00],
        'This Guy': [1.00, 100000], 'That Gal': [9876.54]})
    donors_A.add_donor('Jersey Mikes', 6, 7.00)
    assert donors_A.names == ['Bob', 'Billy', 'Joe Schmoe', 'This Guy', 'That Gal', 'Jersey Mikes']
    
def test_new_structure():
    donors_A = DonorCollection(**{'Bob': [17.56], 'Billy': [500.00, 1000.00], 'Joe Schmoe': [2.00, 0.03, 45.00],
        'This Guy': [1.00, 100000], 'That Gal': [9876.54]})
    assert donors_A.new_structure[0][0] == {'Donor Name': 'This Guy', '# Gifts': 2, 'Total Given($)': 100001.00,
        'Average Gift': 50000.50}
    assert donors_A.new_structure[0][-1] == {'Donor Name': 'Bob', '# Gifts': 1, 'Total Given($)': 17.56,
        'Average Gift': 17.56}
    donors_A.add_donor('Jersey Mikes', 6, 7.00)
    donors_A.data['Joe Schmoe'].add_donations([1000000])
    assert donors_A.new_structure[0][1] == {'Donor Name': 'This Guy', '# Gifts': 2, 'Total Given($)': 100001.00,
        'Average Gift': 50000.50}
    assert donors_A.new_structure[0][-2] == {'Donor Name': 'Bob', '# Gifts': 1, 'Total Given($)': 17.56,
        'Average Gift': 17.56}

