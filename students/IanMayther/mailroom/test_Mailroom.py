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

def test_new_donor():
    assert new_donor("William Gates") is False

def test_gift_float():
    with pytest.raises(TypeError) as excinfo:
        gift("String")
    excinfo.match("String")

def test_thank_you():
    output = "Thanks Andrew Carnegie for your $77.00 donation."
    assert email("Andrew Carnegie", 77.00) == output

def test_create_report():
    assert create_report(donors) is True

def test_print_report():
    assert print_report(create_report) is True

def test_body_letter():
    text = "Yo, Yo, Yo!"
    assert body_letter == text is True

def test_file_creation():
    assert file_exist == True

def test_quit():
    assert quit() == "quit"