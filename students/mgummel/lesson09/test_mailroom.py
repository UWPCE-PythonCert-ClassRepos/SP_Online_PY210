#! /usr/bin/env python3
from donor_models import *
import pytest

donor_db = {
    "William Gates, III": [653772.32, 12.17],
    "Jeff Bezos": [877.33],
    "Paul Allen": [663.23, 43.87, 1.32],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Marc Benioff": [45023.15, 442.30]
}

def test_average():
    donor1 = Donor("William Gates, III", 653772.32)
    print(donor1._full_name)
    assert donor1.avg_donation == 653772.32

    donor1.add_donation(10.00)
    assert donor1.total_donation == 653782.32
    assert donor1.avg_donation == 653782.32 / 2

    donor1.add_donation(532.79)
    assert donor1.total_donation == 654315.11
    assert donor1.avg_donation == 654315.11 / 3

