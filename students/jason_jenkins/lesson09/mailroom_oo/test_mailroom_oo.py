#!/usr/bin/env python3

"""
Lesson 9: Mail Room Part Object Oriented Tests
Course: UW PY210
Author: Jason Jenkins
"""

from donor_models import Donor, DonorCollection


def test_donor_init():
    d1 = Donor("Jason Jenkins", 124.2456)

    assert d1.full_name == "Jason Jenkins"
    assert d1.total_given == 124.25
    assert d1.num_gifts == 1
    assert d1.average == 124.25

    d2 = Donor("Test", 0)
    d2.give(4)
    d2.give(2)
    d2.give(1)

    assert d2.full_name == "Test"
    assert d2.total_given == 7
    assert d2.num_gifts == 3
    assert d2.average == 2.33


def test_donor_str():
    d1 = Donor("Jason Jenkins", 124)
    assert str(d1) == "Jason Jenkins"


def test_donor_thanks():
    d1 = Donor("Jason Jenkins", 124)
    assert d1.thanks() == "Thank you Jason Jenkins for your donation."


def test_donor_eq():
    d1 = Donor("Jason Jenkins", 124)
    assert d1 == "jason Jenkins"
    assert d1 != "test"


def test_donor_collection_init():
    donors = DonorCollection()
    d1 = Donor("Jason Jenkins", 124.123)
    d2 = Donor("Test", 0)
    donors.append(d1)
    donors.append(d2)

    assert donors[0].full_name == "Jason Jenkins"
    assert donors[0].total_given == 124.12
    assert donors[0].num_gifts == 1
    assert donors[0].average == 124.12

    assert donors[1].full_name == "Test"
    assert donors[1].total_given == 0
    assert donors[1].num_gifts == 0
    assert donors[1].average == 0


def test_donor_collection_get_report():
    donors = DonorCollection()

    will_gates = Donor("William Gates", 1345.462)

    mark_zuck = Donor("Mark Zuckerberg", 12546.124)
    mark_zuck.give(13445.124)

    jeff_bezo = Donor("Jeff Bezos", 1234.123)
    jeff_bezo.give(12341431.12)

    paul_allen = Donor("Paul Allen", 734.12)
    paul_allen.give(124.41)
    paul_allen.give(10000)

    jason_jenkins = Donor("Jason Jenkins", 10)
    jason_jenkins.give(20)
    jason_jenkins.give(30)
    jason_jenkins.give(40)
    jason_jenkins.give(50)
    jason_jenkins.give(60)

    donors.append(will_gates)
    donors.append(mark_zuck)
    donors.append(jeff_bezo)
    donors.append(paul_allen)
    donors.append(jason_jenkins)

    expected = []
    expected.append(["Jeff Bezos", 12342665.24, 2, 6171332.62])
    expected.append(["Mark Zuckerberg", 25991.25, 2, 12995.62])
    expected.append(["Paul Allen", 10858.53, 3, 3619.51])
    expected.append(["William Gates", 1345.46, 1, 1345.46])
    expected.append(["Jason Jenkins", 210.00, 6, 35.00])

    assert donors.get_report() == expected


def test_donor_collection_donate_lookup():
    donors = DonorCollection()

    assert not donors.lookup("William Gates")

    donors.donate("William Gates", 20)

    assert donors.lookup("william gates")

    assert donors[0].full_name == "William Gates"
    assert donors[0].total_given == 20
    assert donors[0].num_gifts == 1
    assert donors[0].average == 20

    donors.donate("william Gates", 10)

    assert donors[0].full_name == "William Gates"
    assert donors[0].total_given == 30
    assert donors[0].num_gifts == 2
    assert donors[0].average == 15
