#!/usr/bin/env python3

from donor_models import Donor, DonorCollection
import os
import pytest

"""
test code for mailroom_oo
"""

def test_init_donor ():
    donor = Donor('Test')
    assert type(donor) is Donor


def test_donor_donation():
    donor1 = Donor('A. Tester', [1.23])
    assert len(donor1.donations) == 1
    assert sum(donor1.donations) == 1.23
    donor2 = Donor('B. Developer', [1.23, 2.34])
    assert len(donor2.donations) == 2
    assert sum(donor2.donations) == 3.57


def test_collection_init():
    donors = DonorCollection()
    assert type(donors) is DonorCollection


def test_collection_add():
    donor = Donor('A. Tester', [1.23])
    donors = DonorCollection()
    donors.add(donor)
    assert 'A. Tester' in donors.donors.keys()
    donor2 = Donor('B. Developer', [1.23, 2.34])
    donors.add(donor2)
    assert 'B. Developer' in donors.donors.keys()


def test_collection_list_donors():
    donors = DonorCollection()
    donors.add(Donor('A. Tester', [1.23]))
    donors.add(Donor('B. Developer', [4.56]))
    print(donors.list_donors())
    assert 'A. Tester' in donors.list_donors()
    assert 'B. Developer' in donors.list_donors()
    assert 'A. Tester\nB. Developer' in donors.list_donors()


