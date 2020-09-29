#!/usr/bin/env python3

#Chris Dela Pena
#UW PCE PY210
#Assignment 5 - Mailroom Part 4 Test
#2020/7/10

import sys
import os
import mailroom4

def test_sort_donors():
    expected = [('William Gates, III', [653772.32, 12.17]),
                ('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
                ('Jeff Bezos', [877.33]),
                ('Paul Allen', [663.23, 43.87, 1.32])
                ]
    assert mailroom4.sort_donors() == expected

def test_format_report():
    i = {"Sundar Pichai": [1000.00, 1000.00]}
    assert mailroom4.format_report(i) == print(f"{'Sundar Pichai':<20}{2000:<15.2f}{2:<15}{1000:<7.2f}")

def test_add_donor():
    mailroom4.add_donor('Tim Cook')
    assert mailroom4.donor_db['Tim Cook'] == []

def test_add_donation():
    mailroom4.add_donation('Tim Cook', 500)
    assert mailroom4.donor_db['Tim Cook'] == [500]

def test_list_donors():
    donor_list = [donor for donor in mailroom4.donor_db.keys()]
    assert mailroom4.list_donors() == print(donor_list)

def test_thank_you():
    letter = ('Dear Sundar Pichai, thank you for your generous donation of $1000. Regards, the Club Owners')
    assert mailroom4.print_thank_you('Sundar Pichai', 1000) == letter

def test_thank_you_bulk():
    #tests if letters are created
    mailroom4.thank_you_bulk()
    assert os.path.exists("Jeff Bezos.txt")
