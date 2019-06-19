#!/usr/bin/env python3

import os, random, string, tempfile, pytest
from datetime import datetime
from donor_models import Donor, DonorCollection

def test_donor_init():
    # Test that donor can be created
    d = Donor('Eleanor Shellstrop')
    # Test that creating a donor with no name raises an error
    with pytest.raises(TypeError):
        d = Donor()

def test_add_donation():
    # Test that donations can be added, and that last/total donations work
    d = Donor('Eleanor Shellstrop')
    donations_to_add = [100., 50., 150.]
    for amount in donations_to_add:
        d.addDonation(amount)
    assert d.donations == donations_to_add
    assert d.lastDonation() == 150.
    assert d.totalDonations() == 300.
    assert d.averageDonation() == 100.
    assert d.numDonations() == 3

def test_empty_donation():
    # Test that a new donor returns $0 for all donation methods
    d = Donor('Eleanor Shellstrop')
    assert d.lastDonation() == 0
    assert d.totalDonations() == 0
    assert d.averageDonation() == 0
    assert d.numDonations() == 0

def test_generate_email():
    # Test that email is properly generated
    d = Donor('Eleanor Shellstrop')
    donations_to_add = [100., 50.]
    for amount in donations_to_add:
        d.addDonation(amount)
    assert d.generateEmail() == """Dear Eleanor Shellstrop,

Thank you for your generous donation of $50.00.
To date, you have donated a total of $150.00 to our charity.
Your contributions help new arrivals receive the highest quality care possible.
Please know that your donations make a world of difference!

Sincerely,
The Good Place Team"""

def test_donorcollection_init():
    # Test that donor collection initializes with empty dict
    dc = DonorCollection()
    assert dc.donors == {}
    assert dc.donorNames == []

def test_add_donor():
    # Test that donors can be added to collection
    dc = DonorCollection()
    dc.updateDonor('Jason Mendoza',25.)
    donors = dc.donors
    assert 'Jason Mendoza' in donors

def test_get_donor():
    # Test that donors can be retrieved from collection
    dc = DonorCollection()
    dc.updateDonor('Jason Mendoza',100.)
    d = dc.getDonor('Jason Mendoza')
    assert isinstance(d,Donor)
    assert d.name == 'Jason Mendoza'
    assert d.lastDonation() == 100.
    # Should return new donor if donor does not exist
    d = dc.getDonor('New Donor')
    assert isinstance(d,Donor)
    assert d.name == 'New Donor'

def test_get_donor_names():
    # Test that list of donor names can be retrieved
    dc = DonorCollection()
    dc.updateDonor('Eleanor Shellstrop',50.)
    dc.updateDonor('Jason Mendoza',25.)
    dc.updateDonor('Chidi Anagonye',100.)
    donors = dc.donorNames
    donors.sort()
    assert donors == ['Chidi Anagonye', 'Eleanor Shellstrop', 'Jason Mendoza']

def test_update_donor():
    # Tests that new donor can be added and updated
    dc = DonorCollection()
    dc.updateDonor('Jason Mendoza',100.)
    dc.updateDonor('Jason Mendoza',200.)
    d = dc.getDonor('Jason Mendoza')
    assert d.lastDonation() == 200.
    assert d.totalDonations() == 300.
    assert d.numDonations() == 2
    assert d.averageDonation() == 150.

def test_report_generation():
    # Test report generation
    dc = DonorCollection()
    donors = ['Eleanor Shellstrop', 'Jason Mendoza', 'Chidi Anagonye']
    amounts = [[50.,25.,75.], [100.,50.,80.], [200.,100.,300.]]
    for donor, amount in zip(donors,amounts):
        for donation in amount:
            dc.updateDonor(donor, donation)
    report = dc.generateReportData()
    assert len(report) == len(donors)
    assert report[-1] == ('Eleanor Shellstrop', 150., 3, 50.)
