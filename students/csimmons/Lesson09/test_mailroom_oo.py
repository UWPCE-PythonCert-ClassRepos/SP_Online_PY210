#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom_oo.py assignment
# Mailroom unit test suite w/ pytest
# Created 1/17/2021 - csimmons

import pytest
from donor_models import *

#Working
def test_donor_init():
    d = Donor(name='Craig', donations= 500)
    print(d.name, d.donations, d)
    assert d.name == 'Craig'
    assert d.donations == 500

#Working
def test_donorcollection_init():
    dc = DonorCollection()
    donate = dc.donors_db.get('Christine Ruotolo')
    donate2 = dc.donors_db.get('David Basilio')
    print(donate, donate2)
    assert donate[0] == 3000
    assert donate2[4] == 5000

# Working
def test_create_DonorObjs():
    dc = DonorCollection()
    for donor, donation in dc.donors_db.items():
        objname = Donor(donor, donation)
        print(objname, donation)
        assert objname.name == donor

# Working
def test_Donor_printables():
    d = Donor(name='Craig', donations= 100)
    print(str(d))
    print(repr(d))
    assert str(d) == 'Donor Name is: Craig'
    assert repr(d) == 'Donor(Craig)'

# Working
def test_DonorCollection_printables():
    dc = DonorCollection()
    print(str(dc))
    print(repr(dc))
    assert str(dc) == 'str: DonorCollection Object'
    assert repr(dc) == 'repr: DonorCollection Object'

#Working
def test_add_donor():
    dc = DonorCollection()
    dc.add_donor('Craig Simmons', 75000)
    dc.add_donor('Anne Francis', 5000)
    assert (dc.donors_db.get('Craig Simmons')) == [75000]
    assert (dc.donors_db.get('Anne Francis')) == [5000]

#Working
def test_total_donations():
    dc = DonorCollection()
    d = Donor('Jen Palkha', [100, 300, 1000, 50, 50])
    vals = dc.donors_db.get('Mary Newcomer')
    e = Donor('Mary Newcomer', vals)
    print(d, d.total_donations, d.number_donations, d.avg_donation)
    print(e, e.total_donations, e.number_donations, e.avg_donation)
    assert d.total_donations == 1500
    assert e.total_donations == 12800

#Working
def test_number_donations():
    dc = DonorCollection()
    d = Donor('Jen Palkha', [100, 300, 1000, 50, 50])
    vals = dc.donors_db.get('Mary Newcomer')
    e = Donor('Mary Newcomer', vals)
    print(d, d.total_donations, d.number_donations, d.avg_donation)
    print(e, e.total_donations, e.number_donations, e.avg_donation)
    assert d.number_donations == 5
    assert e.number_donations == 3

#Working
def test_avg_donation():
    dc = DonorCollection()
    d = Donor('Jen Palkha', [100, 300, 1000, 50, 50])
    vals = dc.donors_db.get('Mary Newcomer')
    e = Donor('Mary Newcomer', vals)
    print(d, d.total_donations, d.number_donations, d.avg_donation)
    print(e, e.total_donations, e.number_donations, e.avg_donation)
    assert d.avg_donation == 300
    assert e.avg_donation == 4266 + 2/3

#Working
def test_donor_list():
    dc = DonorCollection()
    donors = []
    for donor in dc.donors_db.keys():
        donors.append(donor)
    end = dc.donor_list
    assert end == list(donors)

#Working
def test_find_donor():
    dc = DonorCollection()
    find = dc.find_donor('Mary Newcomer')
    find2 = dc.find_donor('Will Fail')
    print(find, find2)
    assert find == True
    assert find2 == False

#Working
def test_totals_donations():
    dc = DonorCollection()
    d = Donor('Jen Palkha', [100, 300, 1000, 50, 50])
    vals = dc.donors_db.get('Mary Newcomer')
    e = Donor('Mary Newcomer', vals)
    print(d, d.total_donations, d.number_donations, d.avg_donation)
    print(e, e.total_donations, e.number_donations, e.avg_donation)
    assert d.total_donations == 1500
    assert e.total_donations == 12800

#Working
def test_create_report():
    dc = DonorCollection()
    dc.create_report()
    print(dc.all_info)
    assert (dc.all_info[0]) == ['Craig Simmons', 75000, 1, 75000.0]
    assert (dc.all_info[4][0]) == 'Christine Ruotolo'
