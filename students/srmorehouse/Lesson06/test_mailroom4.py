#!/usr/bin/env python3

from mailroom4 import *
import os
import pytest

"""
test code for mailroom4

Adapted from the "coding bat" site: https://codingbat.com/python

Return True if the party with the given values is successful,
or False otherwise.
"""

donor_db = {"Bill Gates": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
            }


def test_donor_db ():
    assert list_donors(donor_db) == ['Bill Gates','Jeff Bezos','Paul Allen','Mark Zuckerberg']


def test_add_donor ():
    new_donor_name = "Test"
    add_donor (new_donor_name, donor_db)
    assert list_donors(donor_db) == ['Bill Gates','Jeff Bezos','Paul Allen','Mark Zuckerberg','Test']
    add_donation (new_donor_name, 10, donor_db)


def test_add_donation ():
    assert 10 in donor_db['Test']


def test_send_a_thank_you ():
    expected = '\nTest,\n\nThank you for your donation of $1234.44.\n'
    assert compose_thank_you('Test',1234.44) == expected


def test_create_report ():
    test_donor = {'Test': [1, 2, 3.45]}
    expected = ('\nDonor Name | Total Given | Num Gifts  | Average Gift \n'
                  '-----------------------------------------------------\n'
                  'Test        $       6.45           3  $        2.15\n')
    return_val = create_report(test_donor)
    assert return_val == expected


def test_send_letters ():
    cur_dir = os.getcwd()
    donor_count = len(donor_db)
    print_report (donor_db)
    donor_file_count = len([x for x in os.listdir(cur_dir) if x.endswith('.txt')])
    assert donor_file_count == donor_count

