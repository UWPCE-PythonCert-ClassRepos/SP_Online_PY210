#!/usr/bin/env python3

# ------------------------------ #
# Lesson 9 (Mailroom OO) for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 10/23/2019, Created Test Harness
# ------------------------------ #

import pytest
from cli_main import *
from donor_models import *

obj_collection = DonorCollection()

d1 = Donor(2, "Breeanna")
d2 = Donor("1", "Planica")

def test_donor_model():
    assert d1.id == int(2)
    assert d2.id == int(1)
    assert d1.name == "Breeanna"
    assert d2.name == "Planica"
    assert d1._donations == []
    assert d2._donations == []


def test_add_donation():
    d1.add_donation(5.50)
    d2.add_donation(5.50, 5.25)
    assert d1._donations == [5.50]
    assert d2._donations == [5.50, 5.25]


def test_collection_init():
    assert obj_collection.collection == []


def test_append_collection():
    obj_collection.append_collection(d1)
    obj_collection.append_collection(d2)
    assert obj_collection.collection[0] == d1
    assert obj_collection.collection[1] == d2


def test_list_current():
    header = "\nDonorID, DonorName\n------------------\n"
    data = "1, Planica\n2, Breeanna\n"
    assert obj_collection.list_current() == header + data


def test_next_id():
    d3 = Donor(obj_collection.next_id(), "Bree")
    assert d3.id == int(3)


def test_ordinal_freq():
    assert obj_collection.ordinal_freq(1) == "1st"
    assert obj_collection.ordinal_freq(22) == "22nd"
    assert obj_collection.ordinal_freq(3) == "3rd"
    assert obj_collection.ordinal_freq(13) == "13th"
    assert obj_collection.ordinal_freq(5) == "5th"


def test_total_given():
    assert obj_collection.total_given([1, 1, 1, 1, 1]) == 5
    assert obj_collection.total_given([1, 2, 3, 4]) == 10
    assert obj_collection.total_given([1, 3, 5]) == 9


def test_create_report():
    header = "\nDonor Name                    |Total Given    |Num Gifts |Average Gift   "
    header2 = "\n-------------------------------------------------------------------------\n"
    data = "Planica                       |          10.75|         2|           5.38\n"
    data2 = "Breeanna                      |           5.50|         1|           5.50\n"
    assert obj_collection.create_report() == header + header2 + data + data2
