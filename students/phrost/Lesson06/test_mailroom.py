#!/usr/bin/env python3

import mailroom
from mailroom import *
import os
import pytest

mailroom.donor_db = mailroom.get_donor_db()


def test_donor_db ():
    assert list_donors(donor_db) == ['Jimmy Hendrix','Jack White','Keith Richards','Jimmy Page','Albert Hamond']


def test_add_donor ():
    new_donor_name = "Test"
    add_donor (new_donor_name, donor_db)
    assert list_donors(donor_db) == ['Jimmy Hendrix','Jack White','Keith Richards','Jimmy Page','Albert Hamond','Test']
    add_donation (new_donor_name, 10, donor_db)


def test_add_donation ():
    assert 10 in donor_db['Test']


def test_send_a_thank_you ():
    expected = '\nTest,\n\nThank you for your donation of $400.88.\n'
    assert compose_thank_you('Test',400.88) == expected

