#!/usr/bin/env python

import pytest
from mailroom_oo import Donor


def test_don_init():
    d1 = Donor("DJ Cool Buttz", [69])
    d2 = Donor("DJ CB JR", [420, 80])
    assert d1.name == "DJ Cool Buttz"
    assert d2.name == "DJ CB JR"
    assert sum(d1.donations) == 69
    assert sum(d2.donations) == 500
