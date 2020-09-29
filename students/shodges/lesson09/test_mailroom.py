#!/usr/bin/env python3

import pytest
from donor_models import *
from pathlib import Path

def test_donor_structure():
    """
    Test basic Donor creation.  Validate that the Donor object is instantiated, including
    with optional pre-staged donations.  Validate that count and donations properties are
    immutable.
    """
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
    """
    Process a donation and validate that the count and donations properties properly reflect
    the changes.
    """
    honest_abe = Donor('Abraham Lincoln')

    assert honest_abe.count == 0
    assert honest_abe.donations == 0.0

    honest_abe.process(307.65)

    assert honest_abe.count == 1
    assert honest_abe.donations == 307.65


def test_donor_collection():
    """
    Test DonorCollection class and persistence (since it's using shelve as a db)
    """
    simplecharity = DonorCollection('unit_tests')

    # Since this DB will persist, we want to start with a blank slate, but the del_donor
    # method will raise a KeyError if we try to delete a donor that doesn't exist.  That's
    # ok -- we'll just pass through it.
    try:
        simplecharity.del_donor('Test McTesterson')
    except KeyError:
        pass

    # Validate that the donor doesn't exist
    with pytest.raises(KeyError):
        simplecharity.donor('Test McTesterson')

    # Validate that we can add the donor
    assert simplecharity.add_donor('Test McTesterson') is True

    # Validate that we can process a donation and that its values will persist a DB close/
    # reopen
    simplecharity.donor('Test McTesterson').process(101.01)
    assert simplecharity.donor('Test McTesterson').count == 1
    assert simplecharity.donor('Test McTesterson').donations == 101.01

    # Close the DB and verify that it truly is closed
    simplecharity.db_close()
    with pytest.raises(ValueError):
        simplecharity.donor('Test McTesterson').count

    simplecharity = DonorCollection('unit_tests')
    assert simplecharity.donor('Test McTesterson').count == 1
    assert simplecharity.donor('Test McTesterson').donations == 101.01

    assert simplecharity.del_donor('Test McTesterson') is True

    simplecharity.db_close()


def test_report_generation():
    """
    Test generate_report() method of DonorCollection class.  It's expected this will return
    a dict with each of the donors' names, total gifts, average gifts, and count of gifts.
    """
    simplecharity = DonorCollection('unit_tests')

    assert simplecharity.add_donor('George Washington') is True
    assert simplecharity.add_donor('John Adams') is True
    assert simplecharity.add_donor('Thomas Jefferson') is True

    simplecharity.donor('George Washington').process(1.00)
    simplecharity.donor('George Washington').process(102.37)

    simplecharity.donor('John Adams').process(87.00)

    simplecharity.donor('Thomas Jefferson').process(32.50)

    report = simplecharity.generate_report()

    assert len(report) == 3

    assert report['George Washington']['total'] == 103.37
    assert report['George Washington']['count'] == 2
    assert report['George Washington']['average'] == 51.685

    assert report['John Adams']['total'] == 87.00
    assert report['John Adams']['count'] == 1
    assert report['John Adams']['average'] == 87.00

    assert report['Thomas Jefferson']['total'] == 32.50
    assert report['Thomas Jefferson']['count'] == 1
    assert report['Thomas Jefferson']['average'] == 32.50

    donorlist = simplecharity.donors

    assert 'George Washington' in donorlist
    assert 'John Adams' in donorlist
    assert 'Thomas Jefferson' in donorlist

    assert simplecharity.del_donor('George Washington') is True
    assert simplecharity.del_donor('John Adams') is True
    assert simplecharity.del_donor('Thomas Jefferson') is True

    simplecharity.db_close()


def test_letter_generation():
    """
    Test format_letter() method of Donor class.  It's expected that this will return a
    formatted letter with the donor's most recent donation and total donations.
    """
    simplecharity = DonorCollection('unit_tests')

    assert simplecharity.add_donor('Benjamin Franklin') is True
    simplecharity.donor('Benjamin Franklin').process(13.50)
    simplecharity.donor('Benjamin Franklin').process(26.495)

    letter = simplecharity.donor('Benjamin Franklin').format_letter()

    assert "Dear Benjamin Franklin," in letter
    assert "thank you for your recent gift of $26.50" in letter
    assert "Your very generous gifts of $40.00" in letter

    assert simplecharity.del_donor('Benjamin Franklin') is True

    simplecharity.db_close()


def test_letter_saving():
    """
    Test save_letters() method of DonorCollection class, which will iteratively call
    each Donor's save_letter() method.  Validate the presence of each file.  Content test
    coverage is provided by test_letter_generation as content is provided by the same shared
    function.
    """
    simplecharity = DonorCollection('unit_tests')

    assert simplecharity.add_donor('Winston Churchill') is True
    assert simplecharity.add_donor('Franklin D. Roosevelt') is True

    simplecharity.donor('Winston Churchill').process(87.50)
    simplecharity.donor('Franklin D. Roosevelt').process(20.00)

    letters = simplecharity.save_letters('.')

    for i in range(0, len(letters[1])):
        assert Path(letters[1][i]).exists() is True
        Path(letters[1][i]).unlink()

    assert len(letters[2]) == 0

    Path(letters[0]).rmdir()

    assert simplecharity.del_donor('Winston Churchill') is True
    assert simplecharity.del_donor('Franklin D. Roosevelt') is True

    simplecharity.db_close()
