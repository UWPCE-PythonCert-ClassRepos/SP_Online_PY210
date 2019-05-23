#!/usr/bin/env python3

from mailroom import donors, generate_email, get_donors, update_donor

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

# Test new donor
def test_new_donor():
    update_donor('Janet',250.0)
    assert donors['Janet'][-1] == 250.0

# Test update existing donor
def test_update_donor():
    update_donor('Tahani Al-Jamil',1000.0)
    assert donors['Tahani Al-Jamil'][-1] == 1000.0
