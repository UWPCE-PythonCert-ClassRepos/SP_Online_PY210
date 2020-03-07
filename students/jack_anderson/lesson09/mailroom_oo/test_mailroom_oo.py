#!/usr/bin/env python

"""
Jack Anderson
03/05/2020
UW PY210
Lesson 09
Unit tests for Donor and DonorClass classes as well as CLI functions
"""

import pytest
from datetime import date
from donor_models import *
import os


def test_donor_init():
    c = Donor("david")
    print(c.name, c.donations)
    assert c.name == "David"
    assert c.donations == []

    c2 = Donor("jACk aNderSOn", [5])
    print(c2.name, c2.donations)
    assert c2.name == "Jack Anderson"
    assert c2.donations == [5]


    c3 = Donor("David", [1,2,3])
    print(c3.donations)
    assert c3.donations == [1,2,3]
    # assert False
    # assert False

def test_add_donation():
    c = Donor("bob")
    c.add_donation(5)
    print(c.donations)
    assert c.donations == [5]

    c1 = Donor("David", (1, 2, 3))
    c1.add_donation(10)
    print(c1.donations)
    assert 10 in c1.donations
    assert c1.donations == [1, 2, 3, 10]

    # assert False
    # assert False

def test_sum_donations():
    c = Donor('Jim', (2, 7, 11))
    print(c.sum_donations)
    assert c.sum_donations == 20
    assert c.sum_donations == sum(c.donations)

    c1 = Donor("bob", (3.33, 2.25, 2.75))
    print(c1.sum_donations)
    assert c1.sum_donations == sum(c1.donations)

    # assert False
    # assert False

def test_num_donations():
    c = Donor("pete", [2])
    print(c.num_donations)
    assert c.num_donations == len(c.donations)

    c.add_donation(10)
    print(c.num_donations)
    assert c.num_donations == len(c.donations)

    c1 = Donor('Jim', (2, 7, 11))
    print(c1.num_donations)
    assert c1.num_donations == len(c1.donations)

    c2 = Donor('sarah')
    print(c2.num_donations)
    assert c2.num_donations == len(c2.donations)

    # assert False
    # assert False

def test_avg_donation():
    c = Donor('Jim', (4, 5, 6))
    print(c.avg_donation)
    assert c.avg_donation == 5
    assert c.avg_donation == c.sum_donations / c.num_donations

    c1 = Donor("jack", [2.50, 3.50, 4.25, 1.25])
    print(c1.avg_donation)
    assert c1.avg_donation == c1.sum_donations / c1.num_donations

    # assert False
    # assert False

def test_report_template():
    c = Donor('Jim', (4, 5, 6))
    print(c.report_template())
    template = '{name:<21}\t$ {total:>{width}.2f}\t{count:^{width}}\t$ {avg:>{width}.2f}'.format(
        name='Jim', total=15, count=3, avg=5.00, width=10)
    assert c.report_template() == template

    # assert False
    # assert False





donors_list = [['bob', [1, 2, 3]],['sam', [4, 5, 6]],['sally', [7, 8, 9]]]

def test_donor_collection_init():
    validate_1 = donors_list[-1]
    validate_2 = donors_list[0]
    dc = DonorCollection(donors_list)
    print(dc.donors_dict['sally'])
    print(validate_1[-1])
    assert dc.donors_dict['sally'] == validate_1[-1]

    print(dc.donors_dict['bob'])
    print(validate_2[-1])
    assert validate_2[-1] == dc.donors_dict['bob']

    assert 'sam' in dc.donors_dict
    assert 5 in dc.donors_dict['sam']

    # assert False
    # assert False

def test_add_donor():
    dc = DonorCollection(donors_list)
    print(dc.donors_dict)
    dc.add_donor('mark', 100)
    print(dc.donors_dict)
    assert 'mark' in dc.donors_dict
    assert dc.donors_dict['mark'] == 100

    dc.add_donor("sam", 10)
    print(dc.donors_dict['sam'])
    assert dc.donors_dict['sam'] == [4, 5, 6, 10]

    # assert False
    # assert False

def test_list_donors():
    dc = DonorCollection(donors_list)
    print(dc.list_donors())
    assert 'bob' in dc.list_donors()

    # assert False
    # assert False

def test_report_header():
    dc = DonorCollection(donors_list)
    print(dc.report_header())

    template = header = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}'\
        .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10)
    line = "=" * 70
    assert dc.report_header() == '\n' + template + '\n' + line

    # assert False
    # assert False

def test_sort_donors():
    dc = DonorCollection(donors_list)
    print(dc.sorted_dict)

    assert dc.sorted_dict[0] > dc.sorted_dict[1]

    # assert False
    # assert False


def test_create_report():
    dc = DonorCollection(donors_list)
    print(dc.report_header())
    for i in dc.create_report():
        print(i)
    x = dc.create_report()

    assert x[0] > x[1]

    # assert False
    # assert False