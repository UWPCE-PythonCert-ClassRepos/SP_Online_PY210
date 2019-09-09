#!/usr/bin/env python3

# ------------------------------ #
# Test for Assignment 5, Mailroom Part 4
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 9/8/2019, Created Test Harness
# ------------------------------ #

import pytest
from mailroom4 import *

def test_send_thank_you():
    assert send_thank_you("Exit") is None


def get_donation():
    assert get_donation("Exit") is None


def test_current_donors():
    expected = "\nCurrent donors are: Bill Gates, Mark Zuckerberg, Jeff Bezo, Paul Allen, M Bezo"
    assert current_donors() == expected


def test_ordinal_freq():
    assert ordinal_freq(1) == "1st"
    assert ordinal_freq(22) == "22nd"
    assert ordinal_freq(3) == "3rd"
    assert ordinal_freq(13) == "13th"
    assert ordinal_freq(5) == "5th"


def test_total_given():
    assert total_given([1, 1, 1, 1, 1]) == 5
    assert total_given([1, 2, 3, 4]) == 10
    assert total_given([1, 3, 5]) == 9


def test_create_report():
    expected = [('Bill Gates', 653784.48, 2, 326892.24), 
('Mark Zuckerberg', 16396.17, 3, 5465.39), ('Jeff Bezo', 877.33, 1, 877.33), 
('Paul Allen', 708.42, 3, 236.14), ('M Bezo', 110463.25, 1, 110463.25)]
    assert create_report() == expected


def test_update_list():
    expected = {"bill gates": ("Bill Gates", [326892.24, 326892.24]),
"mark zuckerberg": ("Mark Zuckerberg", [5465.39, 5465.39, 5465.39]),
"jeff bezo": ("Jeff Bezo", [877.33]),
"paul allen": ("Paul Allen", [236.14, 236.14, 236.14]),
"m bezo": ("M Bezo", [110463.25]), "bree planica": ("Bree Planica", [200.5567])}
    assert update_list("Bree Planica", 200.5567) == expected