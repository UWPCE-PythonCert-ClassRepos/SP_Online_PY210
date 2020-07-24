#!/usr/bin/env python3

import pytest
from donor_models import *


##################################
# Test Donor class
##################################
def test_init():
    """ test Donor class object initiation """
    donor = Donor("Bill Gates", [40000.00, 50000.00, 9000.00])
    assert isinstance(donor, Donor)
    assert repr(donor) == 'Donor("Bill Gates")'


def test_properties():
    """ test Donor class object properties"""
    donor = Donor("Bill Gates", [40000.00, 50000.00, 9000.00])
    assert donor.name == 'Bill Gates'
    assert donor.donation == [40000.00, 50000.00, 9000.00]
    assert donor.total_donation == 99000
    assert donor.num_donations == 3
    assert donor.avg_donation == 33000


def test_methods():
    """ test Donor class object methods """

    # sort_key method
    donor = Donor("Bill Gates", [40000.00, 50000.00, 9000.00])
    assert donor.sort_key() == 99000

    # method to add a donation amount to an existing donor
    donor.add_donation(5000.00)
    assert donor.donation == [40000.00, 50000.00, 9000.00, 5000.00]

    # method to generate email text string
    assert donor.email_text() == '-'*60 + \
                                 '\nDear Bill Gates,' + \
                                 '\n\nThank you for your generous donation of' + \
                                 f' $5000.00.' + \
                                 '\n\nSincerely,' + \
                                 '\nThe Team\n' + \
                                 '-'*60


##################################
# Test DonorCollection class
##################################
donor = Donor("Bill Gates", [40000.00, 50000.00, 9000.00])
donation_list = [donor]
donor = Donor("Mark Zuckerberg", [10000.00, 6500.00])
donation_list.append(donor)
donor = Donor("Jeff Bezos", [1000.00, 40000.00, 7500.00])
donation_list.append(donor)
donor = Donor("Paul Allen", [100000.00, 2000.00])
donation_list.append(donor)
donor = Donor("Jack Ma", [15000.00, 77000.00])
donation_list.append(donor)

donor_list = DonorCollection(donation_list)


def test_init_dc():
    """ test DonorCollection class object initiation """
    assert isinstance(donor_list, DonorCollection)
    assert repr(donor_list) == 'DonorCollection([Donor("Bill Gates"), ' \
                               'Donor("Mark Zuckerberg"), Donor("Jeff Bezos"), ' \
                               'Donor("Paul Allen"), Donor("Jack Ma")])'


def test_list_donors():
    """ test method to list all donor names """
    assert donor_list.list_donors() == ["Bill Gates", "Mark Zuckerberg", "Jeff Bezos",
                                        "Paul Allen", "Jack Ma"]


def test_add_donor():
    """ test the method to add a donor object """
    donor_list.add_donor(Donor(("john smith").title(), 1))

    assert donor_list.donor_list[-1].name == "John Smith"
    assert donor_list.donor_list[-1].donation == [1]


def test_search_donor():
    """ test search_donor method """
    donor_name = "jack ma"
    existing_donor = donor_list.search_donor(donor_name)
    assert existing_donor is not None
    assert existing_donor.name == "Jack Ma"


def test_get_report():
    """ test get_report method """
    report = donor_list.get_report()

    assert report[0] == 'Donor Name          |  Total Given | Num Gifts |   Average Gift'
    assert report[2] == 'Paul Allen           $   102000.00           2  $      51000.00'
