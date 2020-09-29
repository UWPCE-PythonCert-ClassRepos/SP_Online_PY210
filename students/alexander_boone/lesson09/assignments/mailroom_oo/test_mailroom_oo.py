#!/usr/bin/env python

import pytest
from donor_models import Donor, DonorCollection


# Donor Tests


def test_donor_init():
    """Test Donor object initialization."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor2 = Donor("Alexander", 500, 2)
    assert donor1.fullname == "Alexander Boone"
    assert donor1.firstname == "Alexander"
    assert donor1.lastname == "Boone"
    assert donor1.donation_sum == 500
    assert donor1.donation_count == 2
    assert donor1.donation_avg == 250

    assert donor2.lastname == ""


def test_donor_repr():
    """Test Donor object __repr__ dunder."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor2 = Donor("Alexander", 500, 2)
    assert repr(donor1) == "[Alexander Boone, $500.00, 2, $250.00]"
    assert repr(donor2) == "[Alexander, $500.00, 2, $250.00]"


def test_donor_str():
    """Test Donor object __str__ dunder."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor2 = Donor("Alexander", 500, 2)
    assert str(donor1) == "Donor profile for Alexander Boone"
    assert str(donor2) == "Donor profile for Alexander"


def test_new_donation():
    """Test new donation instance method."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor1.new_donation(1000)
    assert donor1.donation_sum == 1500
    assert donor1.donation_count == 3
    assert donor1.donation_avg == 500


def test_thank_you():
    """Test thank you instance method."""
    donor1 = Donor("Alexander Boone", 500, 2)
    letter = donor1.thank_you()
    assert letter == "\nDear Alexander Boone,\n\n" \
                     "Thank you for your generosity.\n\n" \
                     "You have donated: $500.00" \
                     "\n\nWe are very grateful." \
                     "\n\nBest,\n\n" \
                     "Local Charity\n"


def test_report_row():
    """Test report_row instance method."""
    donor1 = Donor("Alexander Boone", 500, 2)
    row = ('{:<25}{:^5}${:>14,.2f}{:^5}{:>10}{:^5}${:>14,.2f}'
           ).format("Alexander Boone", ' ',
                    500, ' ',
                    2, ' ',
                    250
                    )
    assert donor1.report_row() == row

# DonorCollection Tests


def test_donorcollection_init():
    """Test DonorCollection object initialization."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor2 = Donor("Alexander", 500, 2)
    collection = DonorCollection(donor1, donor2)
    assert collection.names == ["Alexander Boone", "Alexander"]
    assert collection.donors == [donor1, donor2]
    assert collection.data == [repr(donor1), repr(donor2)]


def test_donorcollection_repr():
    """Test DonorCollection object __repr__ dunder."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor2 = Donor("Alexander", 500, 2)
    collection = DonorCollection(donor1, donor2)
    assert repr(collection) == "[Alexander Boone, $500.00, 2, $250.00]" \
                               "\n[Alexander, $500.00, 2, $250.00]"


def test_donorcollection_str():
    """Test DonorCollection object __str__ dunder."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor2 = Donor("Alexander", 500, 2)
    collection = DonorCollection(donor1, donor2)
    assert str(collection) == "A collection of data for " \
                              "the following donors:\n\n" \
                              "Alexander Boone" \
                              "\n" + "Alexander"


def test_donorcollection_append():
    """Test DonorCollection append instance method."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor2 = Donor("Alexander", 500, 2)
    collection = DonorCollection(donor1, donor2)
    donor3 = Donor("New Guy", 1000, 5)
    collection.append(donor3)
    assert len(collection.names) == 3
    assert "New Guy" in collection.names
    assert repr(donor3) in collection.data
    assert donor3 in collection.donors


def test_donorcollection_report():
    """Test DonorCollection report instance method."""
    donor1 = Donor("Alexander Boone", 500, 2)
    donor2 = Donor("Alexander", 1200, 2)
    collection = DonorCollection(donor1, donor2)
    h = ['Donor Name', '|', 'Total Given', '|', 'Num Gifts',
         '|', 'Average Gift']
    report_headers = '{:<25}{:^5}{:<15}{:^5}{:<10}{:^5}{:<15}'.format(*h)
    table_divider = '-' * 80
    report_test = "\n" + report_headers + "\n" \
                  + table_divider + "\n" \
                  + "\n".join([donor.report_row() for
                              donor in collection.donors]) \
                  + "\n"
    report = collection.report()
    assert report == report_test
    assert "Alexander Boone" in report
    assert "500.00" in report
    assert "2" in report
    assert "250.00" in report
    assert "1,200.00" in report
