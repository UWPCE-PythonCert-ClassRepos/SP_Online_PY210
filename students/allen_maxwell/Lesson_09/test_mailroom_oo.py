#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 1/20/2020
# test_mailroom_oo.py

import os
import pytest
from donor_models import *


def test_donor_init():

    d1 = Donor('Tom Sawyer', [120000.5, 2])
    assert d1._name == 'Tom Sawyer'
    assert d1._donations == [120000.5, 2]

    d2 = Donor('john paul jones', [100.0235648425, 1])
    assert d2._name == 'John Paul Jones'
    assert d2._donations == [100.0235648425, 1]

    d3 = Donor('ted Nudget', [1500, 3])
    assert d3._name == 'Ted Nudget'
    assert d3._donations == [1500, 3]

    try:
        d = Donor()
    except TypeError:
        pass
    else:
        assert False

    try:
        d = Donor("johnny cash")
    except TypeError:
        pass
    else:
        assert False

    try:
        d = Donor('Johnny Cash', 1500)
    except TypeError:
        pass
    else:
        assert False

    try:
        d = Donor('John', [1300, 10])
    except IndexError:
        pass
    else:
        assert False

    try:
        d = Donor('Johnny Cash', [-1500, 2])
    except AttributeError:
        pass
    else:
        assert False

    try:
        d = Donor('Johnny Cash', [1500, -1])
    except AttributeError:
        pass
    else:
        assert False

    try:
        d = Donor('Johnny Cash', [1500, 0])
    except AttributeError:
        pass
    else:
        assert False

    try:
        d = Donor('Johnny Cash', [0, 1])
    except AttributeError:
        pass
    else:
        assert False


def test_donor_name():
    d1 = Donor('Tom Sawyer', [120000.5, 2])
    assert d1.name == 'Tom Sawyer'
    d2 = Donor('john paul jones', [100.0235648425, 1])
    assert d2.name == 'John Paul Jones'
    d3 = Donor('TED NUDGET', [1500, 3])
    assert d3.name == 'Ted Nudget'


def test_donor_name_setter():
    d = Donor('Tom Sawyer', [120000.5, 2])
    try:
        d.name = "Johnny Cash"
    except AttributeError:
        pass
    else:
        assert False


def test_donor_donations():
    d1 = Donor('Tom Sawyer', [120000.5, 2])
    assert d1.donations == [120000.5, 2]

    d2 = Donor('john paul jones', [100.0235648425, 1])
    assert d2.donations == [100.0235648425, 1]

    d3 = Donor('ted Nudget', [1500, 3])
    assert d3.donations == [1500, 3]


def test_donor_donations_setter():
    d = Donor('ted Nudget', [1500, 3])

    try:
        d.donations = [3000, 3]
    except AttributeError:
        pass
    else:
        assert False


def test_donor_total_donations():
    d1 = Donor('Tom Sawyer', [120000.5, 2, 326892.24])
    assert d1.total_donations == 120000.5

    d2 = Donor('john paul jones', [100.0235648425, 1])
    assert d2.total_donations == 100.0235648425

    d3 = Donor('ted Nudget', [1500, 3])
    assert d3.total_donations == 1500


def test_donor_add_total_donations():
    d = Donor('Tom Sawyer', [120000.5, 2])
    d.add_total_donations(d, 1000.0)
    assert d.total_donations == 121000.5


def test_donor_check_donation_value():
    d = Donor('Tom Sawyer', [120000.5, 2])
    assert d.check_donation_value(1000.0) == 1000

    try:
        d.check_donation_value(0.0)
    except AttributeError:
        pass
    else:
        assert False

    try:
        d.check_donation_value(-1000)
    except AttributeError:
        pass
    else:
        assert False


def test_donor_num_donations():
    d1 = Donor('Tom Sawyer', [120000.5, 2])
    assert d1.num_donations == 2

    d2 = Donor('john paul jones', [100.0235648425, 1.25])
    assert d2.num_donations == 1

    d3 = Donor('ted Nudget', [1500, 3.0])
    assert d3.num_donations == 3


def test_donor_add_num_donations():
    d = Donor('Tom Sawyer', [120000.5, 5])
    d.add_num_donations(d)
    assert d.num_donations == 6


def test_donor_avg_donations():
    d1 = Donor('Tom Sawyer', [120000.5, 2])
    assert d1.avg_donations == (120000.5/2)

    d2 = Donor('john paul jones', [100.0235648425, 1.25])
    assert d2.avg_donations == 100.0235648425

    d3 = Donor('ted Nudget', [1500, 3.0])
    assert d3.avg_donations == (1500/3)


def test_donor_avg_donations_setter():
    d1 = Donor('Tom Sawyer', [120000.5, 2])

    try:
        d1.avg_donations = 326892.24
    except AttributeError:
        pass
    else:
        assert False


def test_donor_new_donation():
    d1 = Donor('Tom Sawyer', [120000.5, 12])
    d1.new_donation(100)
    assert d1.total_donations == 120100.5
    assert d1.num_donations == 13


def test_donor_save_donor_file():
    d = Donor('Tom Sawyer', [120000.5, 12])
    test_letter_text = d.name
    d.save_donor_file(test_letter_text)

    first_name = d.name.split()[0]
    last_name = d.name.split()[1].strip(',')
    file_name = os.path.join("./{}_{}.txt".format(first_name, last_name))
    assert os.path.exists(file_name)
    with open(file_name, 'r') as file_text:
        assert file_text.read() == d.name


dc1 = Donor('Tom Sawyer', [120000.5, 2])
dc2 = Donor('Luke Skywalker', [12, 3])
dc3 = Donor('Johnny Quest', [1800.63, 1])
dc4 = Donor('John Wick', [7200, 3])
dc5 = Donor('James Bond', [100000.02, 2])

test_dict = {
    'Tom Sawyer': [120000.5, 2],
    'Luke Skywalker': [12, 3],
    'Johnny Quest': [1800.63, 1],
    'John Wick': [7200, 3],
    'James Bond': [100000.02, 2]}


def test_donorcollection_init():

    try:
        test_donors = DonorCollection()
    except TypeError:
        assert False

    try:
        test_donors = DonorCollection(dc1, dc2, dc3, dc4, dc5)
    except TypeError:
        assert False

    test_donors = DonorCollection(dc1, dc2, dc3, dc4, dc5)
    for name in test_dict.keys():
        assert test_donors.donors[name].name == name
        assert test_donors.donors[name].donations == test_dict[name]


def test_donorcollection_donors():
    test_donors = DonorCollection(dc1, dc2, dc3, dc4, dc5)
    for name in test_dict.keys():
        assert test_donors.donors[name].name == name
        assert test_donors.donors[name].donations == test_dict[name]


def test_donorcollection_is_donor_present():
    test_donors = DonorCollection(dc1, dc2, dc3, dc4, dc5)
    assert test_donors.is_donor_present('James Bond') is True
    assert test_donors.is_donor_present('Bugs Bunny') is False
    assert test_donors.is_donor_present('James') is False


def test_donorcollection_get_donor_names():
    test_list = ('Tom Sawyer', 'Luke Skywalker', 'Johnny Quest', 'John Wick',
                 'James Bond')
    test_donors = DonorCollection(dc1, dc2, dc3, dc4, dc5)
    i = 0
    for name in test_donors.get_donors_names():
        assert name == test_list[i]
        i += 1


def test_donorcollection_add_donation():
    test_donors = DonorCollection(dc1, dc2, dc3, dc4, dc5)
    test_donors.add_donation('John Wick', 100.25)
    assert dc4.total_donations == 7300.25


def test_donorcollection_get_report():
    test_report = [
        ('Tom Sawyer', 120000.50, 2, 60000.25),
        ('James Bond', 100000.02, 2, 50000.01),
        ('John Wick', 7300.25, 4, 1825.0625),
        ('Johnny Quest', 1800.63, 1, 1800.63),
        ('Luke Skywalker', 12, 3, 4)]

    test_donors = DonorCollection(dc1, dc2, dc3, dc4, dc5)
    report_result = test_donors.get_report()
    for i in range(len(test_report)):
        assert report_result[i] == test_report[i]
