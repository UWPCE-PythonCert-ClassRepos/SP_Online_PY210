#!/usr/bin/env python
# Test for OO Mailroom exercise
from donor_models import *
from cli_main import *


def test_donor_name(): # Test name in Donor class instances

    d_1 = Donor('Bill Gates', [2000000, 250000000])

    assert d_1.name == 'Bill Gates'

def test_donor_donations(): # Test donations list in Donor class object

    d_1 = Donor('Bill Gates', [2000000, 250000000])

    assert d_1.donations == [2000000, 250000000]

    # Test logic for report formating and list functionality
    assert sum(d_1.donations) == 252000000
    assert len(d_1.donations) == 2

def test_add_donation(): # Test donation adds to existing donor

    d_1 = Donor('Bill Gates', [2000000, 250000000])
    d_1.add_donation(12345)

    assert d_1.donations == [2000000, 250000000, 12345]

def test_thank_you_test(): # Test thank you email text
    
    d_1 = Donor('Bill Gates', [2000000, 250000000])
    print(d_1.text_thank_you)
    expected = f'\nDear Bill Gates:\n\nOn behalf of your Local Charity, I would like to thank you for your generous donation. We appreciate your support not only for us but for our cause.\n\nWe wish you all the best,\n\nLocal Charity Persident\n'
    print(expected)
    assert d_1.text_thank_you == expected

def test_add_donor(): # Test new donor is added to the database

    name = 'Elliot Alderson'
    donation = 509
    d_1 = Donor(name, [donation])
    database.add_donor(name, donation)

    assert name in database._database.keys()

#def test_report(): # Test report generations

        
