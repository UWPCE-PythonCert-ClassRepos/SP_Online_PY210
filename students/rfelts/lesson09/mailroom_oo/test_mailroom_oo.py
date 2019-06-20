#!/usr/bin/env python3

# Russell Felts
# Assignment 9 - Mailroom OO Unit Tests

from donor_models import DonorCollection as Donors
from donor_models import Donor as Donor
import datetime
import pytest
from pathlib import Path


def test_new_donor():
    """ Verify a new donor can be created """
    donor = Donor("Bob", [100])

    assert donor.name == "Bob"
    assert donor.donations[0] is 100


def test_new_donor_fail():
    """ Verify a new donor needs a list for amount to be created """
    with pytest.raises(AssertionError):
        Donor("Bob", 100)


def test_add_donation():
    """ Verify a donation can be added to a donor """
    donor = Donor("Bob", [100])
    donor.add_donation(100)

    assert donor.donations == [100, 100]


def test_add_donation_fail():
    """ Verify a donation value can not be added to a donor unless it can be cast to a float """
    donor = Donor("Bob", [100])
    with pytest.raises(ValueError):
        donor.add_donation("tom")


def test_total_donations():
    """ Verify donation total for a donor is correct """
    donor = Donor("Bob", [100])
    donor.add_donation(100)

    assert donor.donations_total == 200


def test_compose_message():
    """ Verify the donor message is correct """
    donor = Donor("Bob", [100])
    donor.add_donation(100)
    assert donor.compose_message == "\nTo: Bob\nSubject: Thank you.\n\nBob thank you for your previous generous " \
                                    "donation of 100.00.\nYour total donations to date are now: 200.00."


def test_write_letter():
    """ Check to see if the requested file is created the file content is checked in test_compose_message """
    donor = Donor("Bob", [100])
    donor.write_letter()

    now = datetime.datetime.now()

    config = Path('Bob' + '_' + str(now.month) + '_' + str(now.year) + '.txt')
    assert config.is_file()


def test_list_donors():
    """ Verify the method creates a string containing the expected donors """
    donors = Donors()
    donor_list = donors.list_donors

    assert donor_list == "\nLionel Messi\nCristiano Ronaldo\nGianluigi Buffon\nNeymar\nPaolo Maldini\n"


def test_get_name_padding():
    """ Verify the method produces the expected int result using the default donor list """
    donors = Donors()
    name_padding = donors.get_name_padding

    assert name_padding is 21


def test_get_donation_padding():
    """ Verify the method produces the expected int result using the default donor list """
    donors = Donors()
    donation_padding = donors.get_donation_padding(['Gianluigi Buffon', 1002500.5, 2, 501250.25])

    assert donation_padding is 14


def test_donor_exists():
    """ Verify the return value for an existing donor using the default list by checking if the return value is a list
    and the list contains the object related to the donor """
    donors = Donors()
    result = donors.donor_exists("Neymar")

    assert isinstance(result, list)
    assert result[0].name == "Neymar"


def test_donor_doesnt_exists():
    """ Verify the return value for a non-existing donor using the default list by checking if the return value is an
    empty list """
    donors = Donors()
    result = donors.donor_exists("Bob")

    assert isinstance(result, list)
    with pytest.raises(IndexError):
        result[0]


def test_add_donor():
    """ Verify a new donor can be added to the donor list"""
    donors = Donors()
    donor = donors.add_donor("Bob", 125.50)

    assert donor.name == "Bob"
    assert donor.donations[0] == 125.50


def test_create_report():
    """ Use the default donor_list to verify the method creates a list of donors containing:
    donor name, total donation amount, number of donation, average donation """
    donors = Donors()
    report_data = donors.create_report()

    assert ['Lionel Messi', 100, 1, 100.0] in report_data
    assert ['Cristiano Ronaldo', 14475, 3, 4825.0] in report_data
    assert ['Gianluigi Buffon', 1002500.5, 2, 501250.25] in report_data
    assert ['Neymar', 405.24, 4, 101.31] in report_data
    assert ['Paolo Maldini', 24039.95, 4, 6009.9875] in report_data

    # The list is sorted by total donation amount so check the first and last items are correct
    assert "Gianluigi Buffon" in report_data[0]
    assert "Lionel Messi" in report_data[4]
