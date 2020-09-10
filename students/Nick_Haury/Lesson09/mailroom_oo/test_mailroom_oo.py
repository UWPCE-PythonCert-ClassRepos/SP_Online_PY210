#!/usr/bin/env python3
import pytest
import donor_models as dm
import cli_main as cm

'''
Test for the object oriented version of the mailroom program.
'''

def test_create_donor():
    # test if a donor can be successfully created
    d1 = dm.Donor("Dude1")
    d2 = dm.Donor("Dude2", [100.00])
    d3 = dm.Donor("Dude3", [100.00, 200.00])

    assert d1.donor_name == "Dude1"
