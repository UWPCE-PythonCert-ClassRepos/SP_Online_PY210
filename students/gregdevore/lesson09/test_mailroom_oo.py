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
    # Test that donations can be added
    d = Donor('Eleanor Shellstrop')
    donations_to_add = [100., 50., 275.]
    for amount in donations_to_add:
        d.add_donation(amount)
    assert d.donations == donations_to_add
