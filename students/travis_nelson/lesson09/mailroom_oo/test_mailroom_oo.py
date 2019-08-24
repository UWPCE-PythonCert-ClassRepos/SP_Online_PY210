#!/usr/bin/env python3

import pytest

from donor_models import *


def test_Donor():
    """Test expected Donor class behavior"""
    d1 = Donor()
    assert isinstance(d1, Donor)

    # Test new donor with a single donation

    d2 = Donor("Count Chocula", 666)
    assert d2.name == "Count Chocula"
    assert d2.donations == [666]
    assert d2.number_donations == 1
    assert d2.most_recent_donation == 666

    # Test new donor with multiple donations

    d3 = Donor("Danny Brown", [23, 32, 12, 55])
    assert d3.name == "Danny Brown"
    assert d3.donations == [23, 32, 12, 55]
    assert d3.number_donations == 4
    assert d3.sum_donations == 122
    assert d3.average_donation == 30.5

    # Test adding donations

    d3.add_donation(111)
    assert d3.donations == [23, 32, 12, 55, 111]
    assert d3.number_donations == 5
    assert d3.most_recent_donation == 111
    