import pytest
from donor_models import *

def test_donors():
    d1 = Donor("Billy Galloway")
    d1.calculate_donations = 100
    d1.calculate_donations = 10
    d1.calculate_donations = 50
    assert d1.fullname == "Billy Galloway"
    assert d1.donation_total == 160
    print(repr(d1))
    print(d1.donor_attributes)
    d2 = Donor.from_donor("larry", 110)
    d2.calculate_donations = 200
    print(d2)
    
    # donors_ = (d1.fullname, d1.donation_total, d1.times_donated, d1.average_donation)
    # print(donors_)
    # d2 = d("billy")
    # d3 = d("gina")
# def test_database():
#     d1 = Donor("Billy")
#     d2 = Donor("Gina")
#     db = DonorCollection(d1)
#     print(db)
    