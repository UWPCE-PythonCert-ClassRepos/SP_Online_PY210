#!/usr/bin/env python3

import pytest

from donor_models import Donor, DonorCollection

# testing Donor model

def test_donor():
    d = Donor("Nathan Explosion")
    assert d.name == "Nathan Explosion"
    assert d.donation_amount == []

def test_add_donation():
    d = Donor("Nathan Explosion", [43])
    assert d.donation_amount == [43]
    d.add_donation(100)
    assert d.donation_amount == [43, 100]

def test_thank_you_letter():
    d = Donor("Nathan Explosion", [100])
    assert 'Nathan Explosion' in d.thank_you_letter()
    assert '100' in d.thank_you_letter()

# testing DonorCollection model

def test_initialize_donor_dict():
    D = DonorCollection()
    donors_dict = {
                    "William": [87470],
                    "Pickles": [87838],
                  }
    