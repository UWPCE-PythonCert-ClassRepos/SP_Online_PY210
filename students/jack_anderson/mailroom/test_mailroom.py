#!/usr/bin/env python

"""
UW
Python210
Jack Anderson
02/19/20

Test Suite for the mailroom program
"""
from datetime import date
from mailroom_pt4 import *

now = date.today()

# SEND THANKS TEST CASES
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
    template = ("Hello Bob,\n\n"
                "Thank you for your recent gift of $100.00! \n"
                "We will use your gift to help with costs for our upcoming play! \n"
                "Thank you for giving!\n\n"
                "Best Regards, \n"
                "The Blanchford Community Center!")
    assert send_email('Bob', 100) == template


# CREATE REPORT TEST CASES
def test_donor_details():
    assert donor_details('Sam Smith', ([5, 10, 50, 20])) == ('Sam Smith', 4, 85, 21.25)

def test_report_header():
    expected = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}' \
        .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10)
    assert report_header() == expected

def test_create_report():
    assert create_report() == report