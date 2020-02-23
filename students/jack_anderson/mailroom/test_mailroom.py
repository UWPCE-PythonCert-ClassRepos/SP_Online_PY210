#!/usr/bin/env python

"""
UW
Python210
Jack Anderson
02/19/20

Test Suite for the mailroom program
"""
import unittest
from datetime import date
from mailroom_pt4 import *

now = date.today()

# SEND THANKS TEST CASES
def test_name_check_valid():
    assert check_name('jack') == "jack"

def test_donation_check_valid_01():
    assert check_donation('500') == 500.0

def test_donation_check_valid_02():
    assert check_donation('800.32') == 800.32

def test_donation_check_invalid_01():
    assert check_donation(800.32) == pytest.raises(TypeError)

def test_list_names():
    assert list_names() == ['Bubbles Trailer', 'Julien Park', 'Ricky Boys', 'Jack Anderson', 'Lacey Coffin Greene']

def test_add_items_new_donor():
    assert add_items('Jerry Ross', 500) == ('Jerry Ross', 500)

def test_get_new_donor_values():
    assert get_donor_values('Jerry Ross') == [500]

def test_add_items_returning_donor():
    assert add_items('Jack Anderson', 500) == ('Jack Anderson',500)

def test_get_returning_donor_values():
    assert get_donor_values('Jack Anderson') == [500, 1044, 2232, 4123.56]

def test_send_thanks_letterl():
    template = 'Hello Bob,\n\nThank you for your recent gift of $100.00! \nWe will use your gift to help with costs for our upcoming play! \nThank you for giving!\n\nBest Regards, \nThe Blanchford Community Center!'

    assert send_email('Bob', 100.00) == template


# CREATE REPORT TEST CASES
def test_donor_details():
    assert donor_details('Sam Smith', ([5, 10, 50, 20])) == ('Sam Smith', 4, 85, 21.25)

def test_report_header():
    expected = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}' \
        .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10)
    assert report_header() == expected

def test_create_report():
    assert create_report() == report

# Create Email File
def test_create_file():
    x = user
    y = date
    email = f"Hello {x}, This is a test"
    with open(f'outgoing_emails/{x}_{y}.txt', 'r') as f:
        f.read()
        assert == email