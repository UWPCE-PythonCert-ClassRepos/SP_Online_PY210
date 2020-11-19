#!/usr/bin/env python3

'''Mailroom testing'''

import tempfile, os, datetime

from donor_models import Donor, DonorCollection
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


def test_generate_email():
    d = Donor('Homer Simpson', 25.50)
    assert d.generate_email(11.75) == '\nDear Homer Simpson,\n\n' \
                                      'Thank you for your generous donation of $11.75.\n' \
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

# def test_get_donor_names():
#     assert get_donor_names() == ['Homer Simpson',
#                                           'Charles Burns',
#                                           'Kent Brockman',
#                                           'Ned Flanders',
#                                           'Barney Gumble']
#
#
# def test_add_donation_existing_donor():
#     add_donation('Homer Simpson', 5.25)
#     assert donors['Homer Simpson'] == [25.15, 5.25]
#
#
# def test_add_donation_new_donor():
#     add_donation('Bart Simpson', 10.00)
#     assert donors['Bart Simpson'] == [10.00]
#
#
#
# def test_letters_all():
#     letters_all()
#     date = datetime.date.today().isoformat()
#     assert all([os.path.exists(name.replace(' ', '_') + f'_{date}' + '.txt') for name in donors])
#
#
