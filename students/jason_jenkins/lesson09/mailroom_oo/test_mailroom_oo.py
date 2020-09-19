#!/usr/bin/env python3

"""
Lesson 9: Mail Room Part Object Oriented Tests
Course: UW PY210
Author: Jason Jenkins
"""

from donor_models import Donor, DonorCollection


def test_donor_init():
    d1 = Donor("Jason Jenkins", 124)

    assert d1.full_name == "Jason Jenkins"
    assert d1.total_given == 124
    assert d1.num_gifts == 1
    assert d1.average == 124

    d2 = Donor("Test", 0)

    assert d2.full_name == "Test"
    assert d2.total_given == 0
    assert d2.num_gifts == 0
    assert d2.average == 0


def test_donor_collection_init():
    dc1 = DonorCollection()
    d1 = Donor("Jason Jenkins", 124)
    d2 = Donor("Test", 0)
    dc1.append(d1)
    dc1.append(d2)

    print(type(dc1[0]))

    assert dc1[0].full_name == "Jason Jenkins"
    assert dc1[0].total_given == 124
    assert dc1[0].num_gifts == 1
    assert dc1[0].average == 124

    assert dc1[1].full_name == "Test"
    assert dc1[1].total_given == 0
    assert dc1[1].num_gifts == 0
    assert dc1[1].average == 0
