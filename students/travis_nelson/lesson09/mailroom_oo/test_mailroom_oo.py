#!/usr/bin/env python3

import pytest
import os

from donor_models import *
from cli_main import *


def test_Donor():
    """Test expected Donor class behavior"""
    d1 = Donor()
    assert isinstance(d1, Donor)

    # Test new donor with a single donation

    d2 = Donor("Count Chocula", 666)
    assert d2.name == "Count Chocula"
    assert d2.donations == [666]
    assert d2.number_donations == 1
    assert d2.most_recent_donation == 666

    # Test new donor with multiple donations

    d3 = Donor("Danny Brown", [23, 32, 12, 55])
    assert d3.name == "Danny Brown"
    assert d3.donations == [23, 32, 12, 55]
    assert d3.number_donations == 4
    assert d3.sum_donations == 122
    assert d3.average_donation == 30.5

    # Test adding donations

    d3.add_donation(111)
    assert d3.donations == [23, 32, 12, 55, 111]
    assert d3.number_donations == 5
    assert d3.most_recent_donation == 111

# Test Donor_Collection class


def test_Donor_Collection():
    dc1 = Donor_Collection()
    d = Donor("Count Chocula", 666)
    assert isinstance(dc1, Donor_Collection)
    assert dc1.number_of_donors == 5
    assert "Jeff Bezos" in dc1.donor_names
    dc1.add_donor(d)
    assert dc1.number_of_donors == 6
    assert "Count Chocula" in dc1.donor_names
    assert dc1.top_donor == "William Gates, III"
    assert dc1.most_active == "Brax Dingle"
    dc1.add_donor("Travis Nelson", 87837)
    assert dc1.existing_donor("Travis Nelson")
    dc1_sort1 = dc1.sort_donors_by_last_name()
    assert dc1_sort1[0].name == "Paul Allen"
    dc1_sort2 = dc1.sort_donors_by_first_name()
    assert dc1_sort2[0].name == "Brax Dingle"
    dc1_sort3 = dc1.sort_donors_by_donation_count()
    assert dc1_sort3[0].name == "Brax Dingle"
    d.add_donation(9999999999)
    dc1_sort4 = dc1.sort_donors_by_total_donation_amount()
    assert dc1_sort4[0].name == "Count Chocula"


# Some previous mailroom tests, now being used to test cli_main


def test_validate_input_donor():
    response = validate_input_donor('5')
    assert response is None
    response = validate_input_donor('list')
    assert response is 'List'
    response = validate_input_donor('Bob')
    assert response is 'Bob'
    response = validate_input_donor(2)
    assert response is None


def test_validate_donation():
    response = validate_donation('5')
    assert response == '5'
    response = validate_donation('invalid')
    assert response is None
    response = validate_donation('323323ks')
    assert response is None
