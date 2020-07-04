# test_mailroom.py
# opcode6502: SP_Online_PY210


import pytest
from donor_models import *


def print_debug_statement(d):
    print('d.name:                ' + str(d.name))
    print('d.donations:           ' + str(d.donations))
    print('d.average_donation:    ' + str(d.average_donation))
    print('d.num_donations:       ' + str(d.num_donations))
    print('d.sum_donations:       ' + str(d.sum_donations))


def test_donor_add_donation():
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


def test_donor_average_donations():
    #
    # Docstring.
    """
    This will test the average amount of donations for a given Donor.
    """
    #
    # Test setup.
    d = Donor('Archie Adams', [150, 300, 450])
    #
    # Debug statement; print data if we fail the assert.
    print_debug_statement(d)
    #
    # Assertion.
    assert d.average_donation == 300


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


def test_donor_num_donations():
    #
    # Docstring.
    """
    This will test how many donations there are for a given Donor.
    """
    #
    # Test setup.
    d = Donor('Archie Adams', [123.45, 678.90, 99.99, 100.01, 0.00])
    #
    # Debug statement; print data if we fail the assert.
    print_debug_statement(d)
    #
    # Assertion.
    assert d.num_donations == 5


def test_donor_sum_donations():
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


def test_donor_thank_you_message():
    #
    # Docstring.
    """
    This will test creating a thank you message.
    """
    #
    # Test setup.
    d = Donor('Archie Adams', [123.45])
    thank_you_message = 'Thank you: Donor: Archie Adams: Amount: $123.45'
    #
    # Debug statement; print data if we fail the assert.
    print_debug_statement(d)
    #
    # Assertion.
    assert d.thank_you_message() == thank_you_message


def test_donor_type():
    #
    # Docstring.
    """
    This will test that new Donor objects are of type Donor.
    """
    #
    # Test setup.
    d = Donor('Archie Adams', [123.45])
    #
    # Debug statement; print data if we fail the assert.
    print_debug_statement(d)
    #
    # Assertion.
    assert type(d) is Donor
