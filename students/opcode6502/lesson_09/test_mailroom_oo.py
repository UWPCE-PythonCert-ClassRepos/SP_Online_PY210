# test_mailroom.py
# opcode6502: SP_Online_PY210


import pytest
from donor_models import *


def print_debug_statement(d):
    print('d.name:            ' + str(d.name))
    print('d.donations:       ' + str(d.donations))


def test_donor_init_donations():
    #
    # Test setup.
    d = Donor('Archie Adams', [123.45])
    #
    # Debug statement; print data if we fail the assert.
    print_debug_statement(d)
    #
    # Assertion.
    assert d.donations == [123.45]


def test_donor_init_name():
    #
    # Test setup.
    d = Donor('Archie Adams')
    #
    # Debug statement; print data if we fail the assert.
    print_debug_statement(d)
    #
    # Assertion.
    assert d.name == 'Archie Adams'


def test_add_donation():
    #
    # Test setup.
    d = Donor('Archie Adams')
    d.add_donation([123.45])
    #
    # Debug statement; print data if we fail the assert.
    print_debug_statement(d)
    #
    # Assertion.
    assert d.donations == [123.45]
