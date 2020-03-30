#!/usr/bin/env python
# mailroom_pt4.py, Python 210, Lesson 06

import os
import mailroom


def test_verify_donor_info():
    '''Verifies the initial donor dictionary contains four entries and each name occurs once.'''
    names = list(mailroom.donors)
    assert len(names) == 4
    assert [names.count(name) == 1 for name in names]
    # assert names.count('Bill Gates') == 1


def test_add_donation():
    '''Verify add_donation function successfully adds a new donor and donation to database'''
    mailroom.add_donation('Lisa Ferrier', 1000)
    assert "Lisa Ferrier" in mailroom.donors
    assert mailroom.donors["Lisa Ferrier"] == [1000]


def test_summarize_donations():
    '''Verify donor summary information is accurate.'''
    assert ['Bill Gates', 17777.76, 3, 5925.92] in mailroom.summarize_donations()
    assert ['Steve Jobs', 9350.75, 3, 3116.92] in mailroom.summarize_donations()
    assert ['Paul Allen', 3250.00, 2, 1625] in mailroom.summarize_donations()


def test_send_thank_yous():
    '''Verifies the send_thank_you function creates letter with text, as expected.'''
    mailroom.send_thank_yous()
    assert os.path.exists('bill_gates.txt')
    assert os.path.exists('paul_allen.txt')
    assert os.path.exists('steve_jobs.txt')
    assert os.path.exists('jeff_bezos.txt')

    expected = ['Dear Bill Gates,\n', "Thank you for your generous donations in the amount of $17777.76 to the Children's Hospital. Many children will benefit from your contribution.\n", 'With gratitude,\n', "Seattle Children's."]
    with open('bill_gates.txt', 'r') as f:
        actual = f.readlines()

    assert expected == actual
