#!/usr/bin/env python3

"""Mailroom testing"""

import tempfile, os, datetime

from donor_models import Donor, DonorCollection
import donor_data
import pytest


# Testing the donor class
def test_init_donor():
    d = Donor('Homer Simpson', 25.50)
    assert d.name == 'Homer Simpson'
    assert d.donations == [25.50]


def test_init_donor_invalid_amount():
    with pytest.raises(ValueError):
        d = Donor('Homer Simpson', 'wrong')


def test_add_donation():
    d = Donor('Homer Simpson', 25.50)
    d.add_donation(15.00)
    assert d.donations == [25.50, 15.00]


def test_add_wrong_donation_type():
    d = Donor('Homer Simpson', 25.50)
    with pytest.raises(ValueError):
        d.add_donation('wrong')


def test_add_negative_donation():
    d = Donor('Homer Simpson', 25.50)
    with pytest.raises(ValueError):
        d.add_donation(-15.0)


def test_generate_email():
    d = Donor('Homer Simpson', 25.50)
    assert d.generate_email == '\nDear Homer Simpson,\n\n' \
                               'Thank you for your generous donation of $25.50.\n' \
                               'Your donation will continue to allow us to put a smile on our patients faces.\n\n' \
                               'Sincerely,\n' \
                               'The Last Laugh Program'


def test_donor_summary():
    d = Donor('Homer Simpson', 25.50)
    d.add_donation(12.25)
    d.add_donation(10.25)
    print(d.summary)
    assert d.summary == ['Homer Simpson', 48, 3, 16]


def test_donor_multi_donation():
    d = Donor.multi_donation('Homer Simpson', [15, 25.25, 100.00])
    assert d.donations == [15, 25.25, 100.00]


def test_donor_multi_donation_with_string():
    with pytest.raises(ValueError):
        d = Donor.multi_donation('Homer Simpson', [15, 'wrong', 100.00])


# DonorCollection Tests

def test_donorcollection():
    c = DonorCollection(Donor('Homer Simpson', 10.00))
    assert isinstance(c.donors['Homer Simpson'], Donor)


def test_add_donation_new_donor():
    c = DonorCollection(Donor('Homer Simpson', 10.00))
    c.add_donor(Donor('Bart Simpson', 15.00))
    assert c.donors['Bart Simpson'].donations == [15.00]
    assert c.donors['Homer Simpson'].donations == [10.00]


def test_donorcollection_add_error():
    c = DonorCollection(Donor('Homer Simpson', 10.00))
    with pytest.raises(TypeError):
        c.add_donor('not donor object')


def test_donorcollection_empty():
    c = DonorCollection()
    assert c.donors == {}


def test_donorcollection_add_existing():
    c = DonorCollection(Donor('Homer Simpson', 10.00))
    # create a duplicate named donor
    d = Donor('Homer Simpson', 20.00)
    # print(c.donors['Homer Simpson'].donations)
    c.add_donor(d)
    # print(c.donors['Homer Simpson'].donations)
    # adding existing donor will add donations to existing donor in database
    assert c.donors['Homer Simpson'].donations == [10.0, 20.0]


def test_donorcollection_donorList():
    dList = []
    dList.append(Donor('Homer Simpson', 10.00))
    dList.append(Donor('Charles Burns', 1.00))
    c = DonorCollection.donorList(dList)
    assert isinstance(c.donors['Homer Simpson'], Donor)
    assert isinstance(c.donors['Charles Burns'], Donor)


def test_donorcollection_donorList_empty():
    with pytest.raises(ValueError):
        c = DonorCollection.donorList([])


def test_donorcollection_donorlist():
    """Test donorColletion creation by donorList method with list inputs from donor_data.donors

    This test is to verify that the donor_data.donors is not modificed, similar to test_get_donor_names,
     but with donorList method
    """
    dList = []
    dList.append(Donor.multi_donation('Homer Simpson', donor_data.donors['Homer Simpson']))
    dList.append(Donor.multi_donation('Charles Burns', donor_data.donors['Charles Burns']))
    dList.append(Donor.multi_donation('Kent Brockman', donor_data.donors['Kent Brockman']))
    c = DonorCollection.donorList(dList)
    assert isinstance(c.donors['Homer Simpson'], Donor)
    assert isinstance(c.donors['Charles Burns'], Donor)
    assert c.donors['Homer Simpson'].donations == [25.15]
    assert c.donors['Charles Burns'].donations == [0.01, 0.05]
    assert c.donors['Kent Brockman'].donations == [105.75, 225.76, 387.90]


def test_donorcollection_donordict():
    print(donor_data.donors)
    c = DonorCollection.donorDict(donor_data.donors)
    print(c.donors)
    assert isinstance(c.donors['Homer Simpson'], Donor)
    assert isinstance(c.donors['Charles Burns'], Donor)


def test_get_donor_names():
    """Test getting donor names from DonorCollection"""
    # Discovered during calling donor_data.donors a second time that the dictionary lists were being mutated.
    # Add copy method to the lists in the values of dictionary to ensure user input lists are not modified.
    print(donor_data.donors)
    c = DonorCollection.donorDict(donor_data.donors)
    assert 'Homer Simpson' in c.donor_names
    assert 'Charles Burns' in c.donor_names
    assert 'Kent Brockman' in c.donor_names
    assert 'Ned Flanders' in c.donor_names
    assert 'Barney Gumble' in c.donor_names


def test_letters_all():
    c = DonorCollection.donorDict(donor_data.donors)
    c.letters_all()
    date = datetime.date.today().isoformat()
    assert all([os.path.exists(name.replace(' ', '_') + f'_{date}' + '.txt') for name in c.donor_names])


def test_create_report():
    c = DonorCollection.donorDict(donor_data.donors)
    report = c.create_report()
    assert report[3].startswith('Ned Flanders')
    assert report[4].startswith('Kent Brockman')
    assert report[5].startswith('Barney Gumble')
    assert report[6].startswith('Homer Simpson')
    assert report[7].startswith('Charles Burns')
