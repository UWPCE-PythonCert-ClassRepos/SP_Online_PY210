#!/usr/bin/env python3

import pytest
import os

from donor_models import Donor, DonorCollection

# testing Donor model

def test_donor():
    d = Donor("Nathan Explosion")
    # checks that a new donor has been created
    assert d.name == "Nathan Explosion"
    # checks the donor has no recorded donation
    assert d.donation_amount == []

def test_add_donation():
    d = Donor("Nathan Explosion", [43])
    assert d.donation_amount == [43]
    d.add_donation(100)
    # checks that the donation amount contains the new donation
    assert d.donation_amount == [43, 100]

def test_thank_you_letter():
    d = Donor("Nathan Explosion", [10, 100])
    # checks if donor name is in thank you letter
    assert 'Nathan Explosion' in d.thank_you_letter()
    # checks that the last donation is in thank you letter
    assert '100' in d.thank_you_letter()

# testing DonorCollection model

donor_dict = {"William": [87470], "Pickles": [87838],}
donors = DonorCollection.initialize_donor_dict(donor_dict)

def test_initialize_donor_dict():
    # checks that there are2 donors
    assert len(donors.donors) == 2
    # checks donation amount for second donor is correct
    assert donors.donors["Pickles"].donation_amount == [87838]

def test_add_donor():
    d = Donor("Erik", [100])
    donors.add_donor(d)
    # checks if the DonorCollection has added a new donor
    assert len(donors.donors) == 3

def test_check_donors():
    # checks to see if a donor donor class will return True
    assert donors.check_donors("Erik") == True
    # checks to see if a non existent donor returns False
    assert donors.check_donors("Fake") == False

def test_list_donors():
    dl = donors.list_donors()
    # checks if the donor list contains line breaks
    assert "\n" in dl

def test_report_of_donors():
    dr = donors.report_of_donors()
    # checks that the report contains the correct number of donors
    assert len(dr) == 3
    # checks that the report is returning the expected number of parameters
    assert len(dr[0]) == 4

