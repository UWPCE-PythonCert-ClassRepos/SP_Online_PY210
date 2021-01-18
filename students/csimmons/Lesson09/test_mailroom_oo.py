#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom_oo.py assignment
# Mailroom unit test suite w/ pytest
# Created 1/17/2021 - csimmons

import pytest
from donor_models import *

def test_donor_init():
    d = Donor(name='Craig', donations= 500)
    assert d.name == 'Craig'
    assert d.donations == 500

def test_donorcollection_init():
    dc = DonorCollection()
    donate = dc.donors_db.get('Christine Ruotolo')
    donate2 = dc.donors_db.get('David Basilio')
    assert donate[0] == 3000
    assert donate2[4] == 5000

def test_create_DonorObjs():
    dc = DonorCollection()
    for donor, donation in dc.donors_db.items():
        objname = Donor(donor, donation)
        assert objname.name == donor

def test_add_donor():
    dc = DonorCollection()
    craig = Donor(name= 'Craig Simmons', donations= 75000)
    dc.donors_db.setdefault(craig.name, []).append(craig.donations)
    gift = dc.donors_db.get('Craig Simmons')
    assert gift == [75000]

def test_total_donations():
    d = Donor()
    dc = DonorCollection()
    report = {}
    for donor, donation in dc.donors_db.items():
        total = sum(donation)
        report.update({donor: total})
    assert report.get('Sutton Keaney') == 34000

def test_number_donations():
    d = Donor()
    dc = DonorCollection()
    report = {}
    for donor, donation in dc.donors_db.items():
        num = len(donation)
        report.update({donor: num})
    assert report.get('Mary Newcomer') == 3

def test_avg_donation():
    d = Donor()
    dc = DonorCollection()
    report = {}
    for donor, donation in dc.donors_db.items():
        avg = sum(donation) / len(donation)
        report.update({donor: avg})
    assert report.get('Martin Acevedo') == 3500

def test_donor_list():
    dc = DonorCollection()
    donor_list = []
    for donor in dc.donors_db.keys():
        donor_list.append(donor)
    assert donor_list == list(dc.donors_db.keys())