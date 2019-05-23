#!/usr/bin/env python3

from mailroom import generate_email, get_donors

# Test database
donors = {'Eleanor Shellstrop':[25.00, 57.00],
            'Chidi Anagonye':[150.00, 300.00, 275.00],
            'Tahani Al-Jamil':[2000.00,7500.00,12000.00],
            'Jason Mendoza':[15.00,40.00,60.00],
            'Mindy St. Claire':[500.00]}

# Test email generation
def test_email():
    assert generate_email('Janet',100.0,500.0) == """Dear Janet,

Thank you for your generous donation of $100.00.
To date, you have donated a total of $500.00 to our charity.
Your contributions help new arrivals receive the highest quality care possible.
Please know that your donations make a world of difference!

Sincerely,
The Good Place Team"""

# Test get donor list
def test_donor_list():
    assert get_donors(donors) == ['Eleanor Shellstrop','Chidi Anagonye','Tahani Al-Jamil','Jason Mendoza','Mindy St. Claire']
