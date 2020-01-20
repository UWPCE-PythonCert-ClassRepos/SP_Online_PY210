#tests for mailroom_oo.py

import pytest
from mailroom_oo import *

def test_donor():
    donor = Donor("Bill", "Gates")
    assert donor._firstName == "Bill"
    assert donor._lastName == "Gates"
    

def test_donation():
    donor = Donor("Bill", "Gates")
    donor.add_donation(500)
    assert donor.donations == [500]


