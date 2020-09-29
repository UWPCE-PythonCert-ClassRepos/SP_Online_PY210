#!/usr/bin/env python3

import os, random, string, pytest
from donor_models import Donor, DonorCollection

def test_donor_init():
    # Test that donor can be created
    d = Donor('Reem Alqaysi')
    # Test that creating a donor with no name raises an error
    with pytest.raises(TypeError):
        d = Donor()

def test_add_donation():
    # Test that donations can be added, and that last/total donations work
    d = Donor('Reem Alqaysi')
    donations_to_add = [100.00, 50.00, 150.00]
    for amount in donations_to_add:
        d.add_donation(amount)
    assert d.donations == donations_to_add
    assert d.last_donation() == 150.00
    assert d.total_donations() == 300.00
    assert d.average_donation() == 100.00
    assert d.num_donations() == 3

def test_empty_donation():
    # Test that a new donor returns $0 for all donation methods
    d = Donor('Reem Alqaysi')
    assert d.last_donation() == 0
    assert d.total_donations() == 0
    assert d.average_donation() == 0
    assert d.num_donations() == 0

def test_generate_email():
    # Test that email is properly generated
    d = Donor('Reem Alqaysi')
    donations = [100.00, 50.00]
    for amount in donations:
        d.add_donation(amount)
    assert d.generate_email() == """Dear Reem Alqaysi,

Thank you for your generous donation of $50.00.
Please know that your donations make a world of difference!

Sincerely,
The Mailroom Team"""

def test_donorcollection_init():
    # Test that donor collection starting with empty dict
    dc = DonorCollection()
    assert dc.donors == {}
    assert dc.donor_names == []

def test_add_donor():
    # Test that donors can be added to collection
    dc = DonorCollection()
    dc.update_donor('Meghanr Tainor',25.)
    donors = dc.donors
    assert 'Meghanr Tainor' in donors

def test_get_donor():
    # Test that donors can be retrieved from collection
    dc = DonorCollection()
    dc.update_donor('Meghanr Tainor',100.0)
    d = dc.get_donor('Meghanr Tainor')
    assert d.name == 'Meghanr Tainor'
    assert d.last_donation() == 100.0


def test_get_donor_names():
    # Test that list of donor names can be retrieved
    dc = DonorCollection()
    dc.update_donor('Meghanr Tainor',50.00)
    dc.update_donor('Demi Lovato',25.00)
    dc.update_donor('Charlie Puth',100.00)
    donors = dc.donor_names
    donors.sort()
    assert donors == ['Charlie Puth', 'Demi Lovato', 'Meghanr Tainor']

def test_update_donor():
    # Tests that new donor can be added and updated
    dc = DonorCollection()
    dc.update_donor('Meghanr Tainor',100.00)
    dc.update_donor('Meghanr Tainor',200.00)
    d = dc.get_donor('Meghanr Tainor')
    assert d.last_donation() == 200.00
    assert d.total_donations() == 300.00
    assert d.num_donations() == 2
    assert d.average_donation() == 150.00

def test_report_generation():
    # Test report generation
    dc = DonorCollection()
    donors = ['Meghanr Tainor', 'Jason Mendoza', 'Chidi Anagonye']
    amounts = [[50.00,25.00,75.00], [100.00,50.00,80.00], [200.00,100.00,300.00]]
    for donor, amount in zip(donors,amounts):
        for donation in amount:
            dc.update_donor(donor, donation)
    report = dc.generate_report_data()
    assert len(report) == len(donors)
    assert report[-1] == ('Meghanr Tainor', 150.00, 3, 50.00)
