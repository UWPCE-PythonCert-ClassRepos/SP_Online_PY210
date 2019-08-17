import pytest
from donor_models import *
from cli_main import *


def test_donor_class():
    '''Make sure a donor object can be created and have a list of donations'''
    dave = Donor('Dave', 1000.00, 2000.00, 500.00)
    assert dave.name == 'Dave'
    assert dave.donations == [1000.0, 2000.0, 500.0]

def test_donation_append():
    dave = Donor('Dave', 1000.00, 2000.00, 500.00)
    dave.new_donation(200.0)
    assert dave.donations == [1000.0, 2000.0, 500.0, 200.0]

def test_donation_summaries():
    dave = Donor('Dave', 1000.00, 2000.00, 300.00)
    assert dave.number_of_donations() == 3
    assert dave.sum_donations() == 3300.0
    assert dave.avg_donation() == 1100.0

#def test_email():
#    dave = Donor('Dave', 1000.00, 2000.00, 300.00)
#    dave.new_donation(200.0)
#    assert dave.email() == "\nDear Dave,\nThank you for your generous donation of $200.00!\n"

def test_donor_dict():
    dave = Donor('Dave', 1000.00, 2000.00, 300.00)
    bob = Donor('Bob', 200.00, 300.00)
    steve = Donor('Steve', 400.00)
    donor_db = DonorCollection(dave, bob, steve)
    assert donor_db.donors == {'Dave': dave, 'Bob': bob, 'Steve': steve}
    assert steve.donations == [400.0]
    donor_db.new_donation('Steve', 50.00)
    assert steve.donations == [400.0, 50.0]
    #Figure out good test for new entry addition
    donor_db.new_donation('Zach', 100.0)
    print(donor_db.donors)
    assert False
