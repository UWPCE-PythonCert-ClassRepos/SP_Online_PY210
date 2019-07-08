#!/usr/bin/env python
"""
Test suite for all the code in mailroom object assignment.
"""

import pytest

from donor_model import *


##########
# Test initializing

def test_init():
    """
    Test we can make a donor object with the name John
    Name is required
    Make sure name can't be set.
    Make sure donation can't be set
    """
    d = Donor('John')

    assert d.name == 'John'

    with pytest.raises(AttributeError):
        d.name = 'Tom'

    with pytest.raises(AttributeError):
        d.donations = 100


def test_add_donation():
    d = Donor('John')

    d.add_donation(100)

    # Test donation attribute
    assert d.donations == [100]

    # Test donation method
    assert d.num_donations == 1

    # Test donation amount can't be empty or zero
    with pytest.raises(TypeError):
        d.add_donation()


# def test_tot_donated():
#     d = Donor('John')

#     d.add_donation(100)

#     d.add_donation(100)