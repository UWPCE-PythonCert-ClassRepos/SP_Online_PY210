#!/usr/bin/env python3
import pytest
import donor_models as dm
import cli_main as cm

'''
Test for the object oriented version of the mailroom program.
'''

d1 = dm.Donor("Dude1")
d2 = dm.Donor("Dude2", [100.00])
d3 = dm.Donor("Dude3", [100.00, 200.00])

def test_create_donor():
    assert d1.name == "Dude1"
    assert d1.donations == []
    assert d2.donations == [100.00]
    assert d3.donations == [100.00, 200.00]

def test_add_donation():
    with pytest.raises(TypeError):
        d1.add_donation("hello")
    d1.add_donation(10)
    d1.add_donation(20.0)
    assert d1.donations == [10, 20.0]