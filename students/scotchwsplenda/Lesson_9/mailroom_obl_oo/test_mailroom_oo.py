#!/usr/bin/env python

import pytest
import mailroom_oo as mro


def test_don_init():
    d1 = mro.Donor("DJ Cool Buttz", [69])
    d2 = mro.Donor("DJ CB JR", [420, 80])
    assert d1.name == "DJ Cool Buttz"
    assert d2.name == "DJ CB JR"
    assert sum(d1.donations) == 69
    assert sum(d2.donations) == 500


def test_add_contribution():
    donors = mro.DonorCollection()
    donors.add_contribution("Funky", [25.0, 50.0])
    donors.add_contribution("Gordian", [30.0, 45.0])
    assert sum(donors.donor_db["Funky"]) == 75.0
    assert donors.donor_db["Funky"] == [25.0, 50.0]
    assert sum(donors.donor_db["Gordian"]) == 75.0


def test_thanks_mail():
    donor = mro.Donor()
    assert donor.thanks_mail("FunkyBaby", 175.00) == ''.join((
        "\nDear FunkyBaby,\n",
        "Thanks for the $175.00 bucks.\n",
        "We'll spend it real good baby.\n"
        ))
