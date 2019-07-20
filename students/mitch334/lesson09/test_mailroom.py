"""Lesson 09 | Mailroom Part 5"""
#!/usr/bin/env python

"""Used to test the mailroom.py file."""

import os
# import pytest
from mailroom import *


def test_create_report():
    assert donors.create_report() == \
f'\nDonor Name                | Total Given | Num Gifts | Average Gift\n\
------------------------------------------------------------------\n\
Jeff Bezos                 $    1510.00           3  $      503.33\n\
Paul Allen                 $    1000.00           1  $     1000.00\n\
Warren Buffet              $     900.00           2  $      450.00\n\
Mark Zuckerberg            $     270.00           3  $       90.00\n\
William Gates, III         $     150.00           2  $       75.00\n'


def test_donors_list_list():
    assert donors.donors_list('list') == \
f'\nWilliam Gates, III\n\
Jeff Bezos\n\
Mark Zuckerberg\n\
Warren Buffet\n\
Paul Allen\n'


def test_donors_list_db():
    assert donors.donors_list('db') == \
f'\nWilliam Gates, III        [100.0, 50.0]\n\
Jeff Bezos                [1000.0, 10.0, 500.0]\n\
Mark Zuckerberg           [200.0, 20.0, 50.0]\n\
Warren Buffet             [600.0, 300.0]\n\
Paul Allen                [1000.0]\n'


def test_add_donation(test_name = 'Matthew Mitchell', test_amount = 250.12):
    current_donor = donors.add_donor(test_name)
    current_donor.add_donation(test_amount)

    assert current_donor.name == test_name
    assert current_donor.donations == [test_amount]

    assert donors.create_report() == \
f'\nDonor Name                | Total Given | Num Gifts | Average Gift\n\
------------------------------------------------------------------\n\
Jeff Bezos                 $    1510.00           3  $      503.33\n\
Paul Allen                 $    1000.00           1  $     1000.00\n\
Warren Buffet              $     900.00           2  $      450.00\n\
Mark Zuckerberg            $     270.00           3  $       90.00\n\
Matthew Mitchell           $     250.12           1  $      250.12\n\
William Gates, III         $     150.00           2  $       75.00\n'


def test_create_email(test_name = 'Matthew Mitchell', test_amount = 250):
    current_donor = donors.add_donor(test_name)

    assert current_donor.create_email(test_amount) == \
f'Dear Matthew Mitchell,\n\nThank you for the generous donation of $250.00.\n\n\
Sincerely,\nMatthew Mitchell'


def test_send_letters():
    donors.send_letters()
    for file in donors.send_letters():
        assert(os.path.isfile(file))
