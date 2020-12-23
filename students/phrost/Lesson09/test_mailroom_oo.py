#!/usr/bin/env python3

from donor_models import Donor, DonorCollection
import os
import pytest


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


def test_donor_add_donation():
    donor1 = Donor('A. Tester', [1.23])
    assert sum(donor1.donations) == 1.23
    donor1.add_donation(1)
    assert sum(donor1.donations) == 2.23
    assert len(donor1.donations) == 2


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


def test_donor_compose_thank_you():
    donor = Donor('Test', [1.23, 2.10])
    assert 'Test' in donor.compose_thank_you()
    assert '2.10' in donor.compose_thank_you()


def test_donor_get_donor_summary():
    donor = Donor('Test', [1.23, 2.10])
    name, total, count, avg = donor.get_donor_summary()
    print(f'name = {name}, total = {total}, count = {count}, avg = {avg}')
    assert name == 'Test'
    assert total == 3.33
    assert count == 2
    assert avg == 1.665


def test_collection_donor_exists():
    donors = DonorCollection()
    donors.add(Donor('Test1', [10]))
    donors.add(Donor('Test2', [27]))
    assert donors.donor_exists('Test1')
    assert donors.donor_exists('Test2')


def test_create_report():
    donors = DonorCollection()
    donors.add(Donor('Tester 01', [1.00, 2.00]))
    expected = ("\nDonor Name                | Total Given | Num Gifts | Average Gift\n"
                "------------------------------------------------------------------\n"
                "Tester 01                  $       3.00           2  $       1.50\n")
    actual = donors.create_report()
    print(actual)
    assert actual == expected


def test_collection_print_report():
    cur_dir = os.getcwd()
    donors = DonorCollection()
    donors.add(Donor('Test1', [10]))
    donors.add(Donor('Test2', [27]))
    donor_count = len(donors.donors)
    donors.print_report()
    donor_file_count = len([x for x in os.listdir(cur_dir) if x.endswith('.txt')])
    assert donor_file_count == donor_count
