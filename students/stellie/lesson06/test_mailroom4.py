#!/usr/bin/env python3

import mailroom4
import os.path

"""Test Mailroom Part 4"""


def test_search_db():
    """Test to see if existing donor in database returns True value"""
    assert mailroom4.search_db('John Smith') is True
    assert mailroom4.search_db('Mary Johnson') is True
    assert mailroom4.search_db('David Carlton') is True
    assert mailroom4.search_db('James Wright') is True
    assert mailroom4.search_db('Caroline Baker') is True


def test_search_db_unregistered():
    """Test to see if unexisting donor in database returns False value"""
    assert mailroom4.search_db('Jane Doe') is False


def test_add_donation():
    """Test expected result when adding donation amount to existing user"""
    mailroom4.donor_db['John Smith'].append(300)
    expected = [10000, 5000, 1000, 300]
    assert mailroom4.donor_db['John Smith'] == expected


def test_add_new_donor():
    """Test expected result when adding new donor and donation to database"""
    mailroom4.donor_db['Ryan Doe'] = [2000]
    expected = [2000]
    assert mailroom4.donor_db['Ryan Doe'] == expected


def test_thank_you_email():
    """Test expected thank you messsage after a donation is made"""
    expected = ('\nThank you Ryan Doe for your generous donation amount of $300.00!')
    assert mailroom4.thank_you_email('Ryan Doe', 300) == expected


def test_create_report():
    """Test expected donor data output after adding new donors and donations"""
    donor_db = {'Ryan Doe': [2000, 2000], 'Jane Doe': [10000]}
    donor_list = list(donor_db.items())
    expected_donor1 = 'Jane Doe             | 10000.00     | 1          | 10000.00       '
    expected_donor2 = 'Ryan Doe             | 4000.00      | 2          | 2000.00        '
    assert mailroom4.create_report(donor_list)[0] == expected_donor1
    assert mailroom4.create_report(donor_list)[1] == expected_donor2


def test_create_letters():
    """Test that donor letters are properly formatted for each donor"""
    


def test_send_letters():
    """Test that files were created for each donor"""
    expected = 'Ryan Doe.txt'
    assert os.path.exists(expected) is True
