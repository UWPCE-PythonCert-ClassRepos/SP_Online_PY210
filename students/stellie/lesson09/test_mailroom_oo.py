#!/usr/bin/env python3

from cli_main import *
from donor_models import *

"""Test code for Object Oriented Mailroom"""


def test_search_db():
    """
    Check for existing and non-existing donor in database.  Test whether or not
    donation amounts are correct for donor.
    """
    assert 'John Smith' in data.data.keys()
    assert 'Alice Wonderland' not in data.data.keys()
    assert data.search_db('James Wright') == [500, 500, 500]


def test_add_donation():
    """Test expected result when adding donation amount to existing donor"""
    Donor('Caroline Baker', data.data.get('Caroline Baker')).add_donation(1000)
    assert data.search_db('Caroline Baker') == [1000, 1000]


def test_add_new_donor():
    """Test expected result when adding new donor and donation to database"""
    data.add_new_donor('Alice Wonderland', 100)
    assert 'Alice Wonderland' in data.data.keys()
    assert data.search_db('Alice Wonderland') == [100]


def test_thank_you_email():
    """Test expected thank you messsage after a donation is made"""
    expected = ('\nThank you Jane Doe for your generous '
                'donation amount of $400.00!')
    assert Donor('Jane Doe', 400).thank_you_email() == expected


def test_create_report():
    """Test expected donor data output after adding new donors and donations"""
    test = {'Ryan Doe': [2000, 2000], 'Jane Doe': [10000]}
    data = DonorCollection(**test)
    expected_donor = 'Jane Doe             | 10000.00     |' + \
                     ' 1          | 10000.00       ' + '\n' + \
                     'Ryan Doe             | 4000.00      |' + \
                     ' 2          | 2000.00        '
    assert '\n'.join(data.create_report()) == expected_donor


def test_donation_count():
    """Test expected number of donations made by a donor"""
    assert Donor('James Wright',
                 data.data.get('James Wright')).donation_count() == 3


def test_total_donations():
    """Test expected sum of donations made by a donor"""
    assert Donor('James Wright',
                 data.data.get('James Wright')).total_donations() == 1500


def test_avg_donations():
    """Test expected average donations amount made by a donor"""
    assert Donor('James Wright',
                 data.data.get('James Wright')).avg_donations() == 500
