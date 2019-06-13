#!/usr/bin/env python3

import os, random, string, tempfile, pytest
from datetime import datetime
from donor_models import Donor

def test_donor_init():
    # Test that donor can be created
    d = Donor('Eleanor Shellstrop')
    # Test that creating a donor with no name raises an error
    with pytest.raises(TypeError):
        d = Donor()

def test_add_donations():
    # Test that donations can be added, and that last/total donations
    d = Donor('Eleanor Shellstrop')
    donations_to_add = [100., 50., 275.]
    for amount in donations_to_add:
        d.add_donation(amount)
    assert d.donations == donations_to_add
    assert d.get_last_donation() == 275.
    assert d.get_total_donations() == 425.

def test_empty_donation():
    # Test that a new donor returns $0 for last and total donations
    d = Donor('Eleanor Shellstrop')
    assert d.get_last_donation() == 0
    assert d.get_total_donations() == 0

def test_generate_email():
    # Test that email is properly generated
    d = Donor('Eleanor Shellstrop')
    donations_to_add = [100., 50.]
    for amount in donations_to_add:
        d.add_donation(amount)
    assert d.generate_email() == """Dear Eleanor Shellstrop,

Thank you for your generous donation of $50.00.
To date, you have donated a total of $150.00 to our charity.
Your contributions help new arrivals receive the highest quality care possible.
Please know that your donations make a world of difference!

Sincerely,
The Good Place Team"""
