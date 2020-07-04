# test_mailroom.py
# opcode6502: SP_Online_PY210


import pytest
from donor_models import *


def test_donor_init_donations():
    #
    # Test setup.
    d = Donor('Archie Adams', [123.45])
    #
    # Assertion.
    assert d.donations == [123.45]


def test_donor_init_name():
    #
    # Test setup.
    d = Donor('Archie Adams')
    #
    # Assertion.
    assert d.name == 'Archie Adams'
