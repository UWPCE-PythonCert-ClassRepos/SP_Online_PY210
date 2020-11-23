#!/usr/bin/env python3

'''Mailroom testing'''

from mailroom import donors, get_donor_names, add_donation, generate_email, generate_report_data, letters_all
import tempfile, os, datetime


def test_get_donor_names():
    assert get_donor_names() == ['Homer Simpson',
                                          'Charles Burns',
                                          'Kent Brockman',
                                          'Ned Flanders',
                                          'Barney Gumble']


def test_add_donation_existing_donor():
    add_donation('Homer Simpson', 5.25)
    assert donors['Homer Simpson'] == [25.15, 5.25]


def test_add_donation_new_donor():
    add_donation('Bart Simpson', 10.00)
    assert donors['Bart Simpson'] == [10.00]


def test_generate_email():
    assert generate_email('Homer Simpson', 11.75) == '\nDear Homer Simpson,\n\n' \
                                                              'Thank you for your generous donation of $11.75.\n' \
                                                              'Your donation will continue to allow us to put a smile on our patients faces.\n\n' \
                                                              'Sincerely,\n' \
                                                              'The Last Laugh Program'


def test_generate_report_data():
    assert generate_report_data()[0] == ['Ned Flanders', 4276.35, 3, 1425.45]


def test_letters_all():
    letters_all()
    date = datetime.date.today().isoformat()
    assert all([os.path.exists(name.replace(' ', '_') + f'_{date}' + '.txt') for name in donors])


