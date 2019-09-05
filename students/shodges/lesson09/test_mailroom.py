#!/usr/bin/env python3

import pytest
from mailroom import *

def test_donor_structure():
    honest_abe = Donor('Abraham Lincoln', 87.00, 18.65)
    teddy = Donor('Theodore Roosevelt')

    assert honest_abe.count == 2
    assert honest_abe.donations == 105.65

    assert teddy.count == 0
    assert teddy.donations == 0

    with pytest.raises(AttributeError):
        teddy.count = 1

    with pytest.raises(AttributeError):
        teddy.donations = 1000000.00


def test_process_donation():
    honest_abe = Donor('Abraham Lincoln')

    assert honest_abe.count == 0
    assert honest_abe.donations == 0.0

    honest_abe.process(307.65)

    assert honest_abe.count == 1
    assert honest_abe.donations == 307.65
