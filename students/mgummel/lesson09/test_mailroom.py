#! /usr/bin/env python3
from donor_models import *
import pytest

# donor_db = {
#     "William Gates, III": [653772.32, 12.17],
#     "Jeff Bezos": [877.33],
#     "Paul Allen": [663.23, 43.87, 1.32],
#     "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
#     "Marc Benioff": [45023.15, 442.30]
# }

def test_average():
    donor1 = Donor("William Gates, III", 653772.32)
    donor2 = Donor("Paul Allen", 663.23)
    assert donor1.avg_donation == 653772.32
    assert donor2.avg_donation == 663.23

    donor1.add_donation(10.00)
    assert donor1.avg_donation == 653782.32 / 2
    assert donor2.avg_donation == 663.23

    donor1.add_donation(532.79)
    donor2.add_donation(368.45)
    assert donor1.avg_donation == 654315.11 / 3
    assert donor2.avg_donation == 1031.68 / 2

def test_total_donation():
    d1 = Donor("Mark Zuckerberg", 1663.23)
    d2 = Donor("Marc Benioff", 45023.15)
    
    assert d1.total_donation == 1663.23
    assert d2.total_donation == 45023.15

    d1.add_donation(100.00)
    d2.add_donation(55.00)
    assert d1.total_donation == 1763.23
    assert d2.total_donation == 45078.15

    d2.add_donation(100.00)
    assert d1.total_donation == 1763.23
    assert d2.total_donation == 45178.15

def test_full_name():
    d1 = Donor("50 Cent", 2343.99)
    d2 = Donor("Meek Mills", 423.10)
    d3 = Donor("Kanye West", 0.01)

    assert d1._full_name == "50 Cent"
    assert d2._full_name == "Meek Mills"
    assert d3._full_name == "Kanye West"

def test_num_of_donations():
    d1 = Donor("50 Cent", 2343.99)
    d2 = Donor("Meek Mills", 423.10)
    d3 = Donor("Kanye West", 0.01)

    assert d1.num_of_donations == 1
    assert d2.num_of_donations == 1
    assert d3.num_of_donations == 1

    d1.add_donation(43.99)
    d3.add_donation(432.10)
    assert d1.num_of_donations == 2
    assert d2.num_of_donations == 1
    assert d3.num_of_donations == 2

    d3.add_donation(42.99)
    assert d1.num_of_donations == 2
    assert d2.num_of_donations == 1
    assert d3.num_of_donations == 3

def test_last_donation():
    d1 = Donor("50 Cent", 2343.99)
    d2 = Donor("Meek Mills", 423.10)
    d3 = Donor("Kanye West", 0.01)

    assert d1.last_donation == 2343.99
    assert d2.last_donation == 423.10
    assert d3.last_donation == 0.01

    d1.add_donation(43.99)
    d3.add_donation(432.10)
    assert d1.last_donation == 43.99
    assert d2.last_donation == 423.10
    assert d3.last_donation == 432.10

    d3.add_donation(42.99)
    assert d1.last_donation == 43.99
    assert d2.last_donation == 423.10
    assert d3.last_donation == 42.99

def test_str():
    d1 = Donor("Kris Smith", 23.43)
    assert ("Kris Smith") in d1.__str__()
    assert ("23.43") in d1.__str__()

    d1.add_donation(417.56)
    assert ("Kris Smith") in d1.__str__()
    assert ("417.56") in d1.__str__()

def test_add_donation():
    d1 = Donor("Kris Smith", 23.43)
    d2 = Donor("Kris Smith Jr.", 42.23)

    assert 23.43 in d1._donations
    assert 42.23 in d2._donations

    d1.add_donation(123456.78)
    assert (123456.78) in d1._donations

    d1.add_donation(987654.23)
    d2.add_donation(7894.76)
    assert (7894.76) in d2._donations
    assert (987654.23) in d1._donations

