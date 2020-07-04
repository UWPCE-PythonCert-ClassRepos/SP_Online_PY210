# test_mailroom.py
# opcode6502: SP_Online_PY210


import pytest
from donor_models import *


def print_debug_statement(d):
    print('d.name:            ' + str(d.name))
    print('d.donations:       ' + str(d.donations))


def test_donor_init_donations():
    #
    # Docstring.
    """
    This will test creating a Donor; specifically that the 'donations' property
    is properly created and set.
    """
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
    # Docstring.
    """
    This will test creating a Donor; specifically that the 'name' property
    is properly created and set.
    """
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
    # Docstring.
    """
    This will test adding a donation for a given Donor.
    """
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


def test_sum_donations():
    #
    # Docstring.
    """
    This will test summing a set of donations for a given Donor.
    """
    #
    # Test setup.
    d = Donor('Archie Adams', [123.45, 678.90, 99.99])
    #
    # Debug statement; print data if we fail the assert.
    print_debug_statement(d)
    #
    # Assertion.
    assert d.sum_donations == 902.34
