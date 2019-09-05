#!/usr/bin/env python3

import pytest
from mailroom import *

def test_donor_structure():
    honest_abe = Donor('Abraham Lincoln', [87.00, 18.65])
    teddy = Donor('Theodore Roosevelt')

    assert honest_abe.count == 2
    assert honest_abe.donations == 105.65

    assert teddy.count == 0
    assert teddy.donations == 0
