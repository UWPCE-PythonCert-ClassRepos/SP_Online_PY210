#!/usr/bin/env python
"""
Test suite for all the code in mailroom object assignment.
"""

import pytest
import os

from donor_model import *


#####################
# Donor Class Tests #
#####################

def test_init():
    """
    Test we can make a donor object with the name John
    Name is required
    Make sure name can't be set.
    Make sure donation can't be set
    """
    # Test adding donor with no amount
    d = Donor('John')

    assert d.name == 'John'

    with pytest.raises(AttributeError):
        d.name = 'Tom'

    with pytest.raises(AttributeError):
        d.donations = 100


def test_add_donation():
    d = Donor('John')

    # Test adding float
    d.add_donation(100.00)
    assert d.donations == [100]
    assert d.num_donations == 1

    # Test adding integer value
    d.add_donation(20)
    assert d.donations == [100, 20]
    assert d.num_donations == 2

    # Test donation amount can't be empty or zero
    with pytest.raises(TypeError):
        d.add_donation()

    # Test donation added can't be negative
    with pytest.raises(ValueError):
        d.add_donation(-100)

    # Test donation is greater than 0
    with pytest.raises(ValueError):
        d.add_donation(0)

    # Test donation has to be a number
    with pytest.raises(ValueError):
        d.add_donation('hello')


def test_tot_donated():
    d = Donor('John')

    d.add_donation(100.00)
    assert d.total_donated == 100

    d.add_donation(100.00)
    assert d.total_donated == 200


def test_average_donation():
    d = Donor('John')

    d.add_donation(100)
    assert d.average_donation == 100

    d.add_donation(50)
    assert d.average_donation == 75


def test_total_ordering():
    d = Donor('John')
    d.add_donation(100)

    d2 = Donor('Tim')
    d2.add_donation(50)

    assert d2 < d


def test_sorting():
    d = Donor('John')
    d.add_donation(10)

    d2 = Donor('Tim')
    d2.add_donation(50)

    d3 = Donor('Beth')
    d3.add_donation(250)

    d4 = Donor('Abby')
    d4.add_donation(5050)

    donor_list = [d3, d, d4, d2]

    donor_list.sort()

    assert donor_list == [d, d2, d3, d4]


def test__str__():
    d = Donor('John')

    print(d)

    strd = d.__str__()

    assert strd == "Donor: John"


def test__repr__():
    d = Donor('John')

    print(d)

    reprd = d.__repr__()

    assert reprd == "Donor(John)"


def test_thank_you():
    d = Donor("John")

    # Test error
    with pytest.raises(RuntimeError):
        d.create_thank_you_note()

    d.add_donation(100)

    thank_you = d.create_thank_you_note()

    assert thank_you == "\nDear John,\n Thank you for your donation of $100.00!\n"


##############################
# DonorCollector Class Tests #
##############################


def test_init_collector():
    DonorRecords = DonorCollection()

    d = Donor('John')
    d.add_donation(10)

    d2 = Donor('Tim')
    d2.add_donation(50)

    d3 = Donor('Beth')
    d3.add_donation(250)

    d4 = Donor('Abby')
    d4.add_donation(5050)

    # Test adding one donor
    DonorRecords.add_donor(d)

    # Test adding multiple donors
    DonorRecords.add_donor(d2, d3, d4)

    # Test all donors got added, also tests the donor property
    assert DonorRecords.donors == {'John', 'Tim', 'Beth', 'Abby'}

    # Test no donor added('No donor added')
    with pytest.raises(UserWarning):
        DonorRecords.add_donor()


def test_report():
    DonorRecords = DonorCollection()

    d = Donor('John')
    d.add_donation(10)

    d2 = Donor('Tim')
    d2.add_donation(50)

    d3 = Donor('Beth')
    d3.add_donation(250)

    d4 = Donor('Abby')
    d4.add_donation(5050)

    DonorRecords.add_donor(d, d2, d3, d4)

    lines = DonorRecords.create_report()
    line = "{:<15} | ${:>13.2f} | {:^11} | ${:>15.2f}"

    # Test lines
    assert lines[0] == '-----Donation Report-----'
    assert lines[1] == '\n{:<15} | {:>14} | {:>11} | {:>16}'.format('Donor Name', 'Total Donation', '# donations', 'Average Donation')
    assert lines[2] == '-'*66
    assert lines[3] == line.format(d4.name, d4.total_donated, d4.num_donations, d4.average_donation)
    assert lines[4] == line.format(d3.name, d3.total_donated, d3.num_donations, d3.average_donation)
    assert lines[5] == line.format(d2.name, d2.total_donated, d2.num_donations, d2.average_donation)
    assert lines[6] == line.format(d.name, d.total_donated, d.num_donations, d.average_donation)


def test__str__DonorCollection():
    DonorRecords = DonorCollection()

    d = Donor('John')
    d.add_donation(10)

    d2 = Donor('Tim')
    d2.add_donation(50)

    d3 = Donor('Beth')
    d3.add_donation(250)

    d4 = Donor('Abby')
    d4.add_donation(5050)

    DonorRecords.add_donor(d, d2, d3, d4)

    dstr = DonorRecords.__str__()
    print(dstr)

    # Test all keys get printed
    assert dstr == "DonorCollection({})".format(DonorRecords.donors)


def test_add_donation_interface():
    DonorRecords = DonorCollection()

    d = Donor('John')
    d.add_donation(10)

    d2 = Donor('Tim')
    d2.add_donation(50)

    d3 = Donor('Beth')
    d3.add_donation(250)

    d4 = Donor('Abby')
    d4.add_donation(5050)

    DonorRecords.add_donor(d, d2, d3, d4)

    # Test adding donation
    DonorRecords.add_donation('Tim', 520)

    # Test Tim's total donation amount got updated
    assert DonorRecords._donors.get('Tim').donations == [50, 520]
    assert DonorRecords._donors.get('Tim').total_donated == 570

    # Test adding zero donation
    with pytest.raises(ValueError):
        DonorRecords.add_donation('Tim', 0)

    # Test adding negative donation
    with pytest.raises(ValueError):
        DonorRecords.add_donation('Tim', -10)

    # Test adding donation for donator not in current DonatorCollector
    DonorRecords.add_donation('Bro', 50)
    DonorRecords.add_donation('Bro2', 150)
    assert DonorRecords.donors == {'Bro2', 'John', 'Tim', 'Abby', 'Beth', 'Bro'}


def test_send_letters():
    DonorRecords = DonorCollection()

    d = Donor('John')
    d.add_donation(10)

    d2 = Donor('Tim')
    d2.add_donation(50)

    d3 = Donor('Beth')
    d3.add_donation(250)

    d4 = Donor('Abby')
    d4.add_donation(5050)

    DonorRecords.add_donor(d, d2, d3, d4)
    DonorRecords.send_letters()

    # Test files
    for donor, data in DonorRecords.items:
        print('In test loop')
        print(DonorRecords.get_donor(donor))
        print(data.total_donated)
        print(f"{donor}.txt")

        # File exists
        assert os.path.isfile(f"{donor}.txt")

        # File contents
        with open(f"{donor}.txt", 'r') as outfile:
            contents = outfile.read()
            print(contents)
            assert contents == f"Dear {donor}\nThank you for your total donation amount of ${data.total_donated}!\nBest wishes,\nThe Team"