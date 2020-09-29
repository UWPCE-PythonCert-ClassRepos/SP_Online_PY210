#!/usr/bin/env python3

# ------------------------------ #
# Test for Assignment 5, Mailroom Part 4
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 9/8/2019, Created Test Harness
# ------------------------------ #

import pytest
from mailroom4 import *

donors = {}

def test_send_thank_you():
    assert send_thank_you("Exit") is None


def get_donation():
    assert get_donation("Exit") is None


def test_update_list():
    donors = {"bree planica": ("Bree Planica", [200.5567])}
    assert update_list("Bree Planica", 200.5567) == donors


def test_current_donors():
    expected = "\nCurrent donors are: Bree Planica"
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
    expected = [('Bree Planica', 200.56, 1, 200.56)]
    assert create_report() == expected

def test_print_thank_you():
    expected = (f"""
Dear Bree Planica,

    We are reaching out to thank you for your 1st donation. We appreciate your 
    continued support. You have donated a total of 200.56 USD. Your recent docation 
    of 200.56 USD will go towards clean food and water for your local citizens 
    in need.
    
    We look forward to seeing you at our upcoming fundraiser event. 

Sincerely, 

The Fundraiser Team
        """)
    assert print_thank_you("Bree Planica", 200.5567) == expected