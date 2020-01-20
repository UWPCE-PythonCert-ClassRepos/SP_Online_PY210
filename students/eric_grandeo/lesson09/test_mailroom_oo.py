#tests for mailroom_oo.py

import pytest
from mailroom_oo import *

def test_donor():
    donor = Donor("Bill", "Gates", 100)
    assert donor._firstName == "Bill"
    assert donor._lastName == "Gates"
    assert donor.donation == 100

    
