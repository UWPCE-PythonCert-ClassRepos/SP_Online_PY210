#tests for mailroom_oo.py

import pytest
from mailroom_oo import *

def test_donor():
    donor = Donor("Bill", "Gates")
    assert donor.name == "Bill Gates"
    
def test_donation():
    donor = Donor("Bill", "Gates")
    donor.add_donation(500)
    assert donor.donations == [500]

def test_sum_donations():
    donor = Donor("Bill", "Gates")
    amounts = [50, 100, 150]
    for amount in amounts:
        donor.add_donation(amount)
    assert donor.sum_donations == 300

def test_num_donations():
    donor = Donor("Bill", "Gates")
    amounts = [50, 100, 150]
    for amount in amounts:
        donor.add_donation(amount)
    assert donor.num_donations == 3

def test_avg_donations():
    donor = Donor("Bill", "Gates")
    amounts = [50, 100, 150]
    for amount in amounts:
        donor.add_donation(amount)
    assert donor.avg_donations == 100


def test_thank_you():
    donor = Donor("Bill", "Gates")
    amounts = [50, 100, 150]
    for amount in amounts:
        donor.add_donation(amount)

    test_result = """
        Dear {name},
        Thank you very much for the generous donation of ${donation:,.2f}
        It is very much appreciated.
        Respectfully,

        Eric G.
        """.format(name="Bill Gates", donation=150)

    assert donor.thank_you == test_result

    