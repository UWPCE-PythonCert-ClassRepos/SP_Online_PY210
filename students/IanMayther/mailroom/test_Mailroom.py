#!/usr/bin/env python3

import pytest

"""
test code for Mailroom

Different scenarios to test:
Thank you:
    Donor Name
    Gift Value
    Letter

Create report:
    create report
    print report

Send Letters:
    Body of letters
    Letters are created

Quit:
    Quits
"""


# you can change this import to test different versions receiver, quit, donors, gift, new_donor, email
from Mailroom import *

@pytest.mark.parametrize(
    'a, expected', [
        ("Morgan Stanely", True),
        ("Cornelius Vanderbilt", True),
        ("John D. Rockefeller", True),
        ("Stephen Girard", True),
        ("Andrew Carnegie", True),
        ("William Gates", False),
        ("Jeffery Bezos", False)
    ]
)
def test_new_donor(a, expected):
    assert new_donor(a) is expected

def test_gift_float():
    assert gift(75.54) == 75.54

def test_gift_string():
    with pytest.raises(ValueError):
        gift("String")

def test_thank_you():
    output = "Thanks Andrew Carnegie for your $77.0 in donations."
    assert thank_you("Andrew Carnegie", 77.00) == output


@pytest.mark.parametrize(
    'a, expected', [
        ("Morgan Stanely", 20.01),
        ("Cornelius Vanderbilt", 825.00),
        ("John D. Rockefeller", 7175.00),
        ("Stephen Girard", 60000.00),
        ("Andrew Carnegie", 1000.03),
    ]
)
def test_calc_report(a, expected):
    assert calc_report[a] == expected

def test_print_report():
    assert print_report(create_report) is True

def test_body_letter():
    text = "Yo, Yo, Yo!"
    assert body_letter == text is True

def test_file_creation():
    assert file_exist == True

def test_quit():
    assert quit() == "quit"