import pytest
from mailroom_oo.donor_models import Donor as d
from mailroom_oo.database import Database as db

def test_donors():
    d1 = d("Billy Galloway")
    database = db(d1)
    print(database.construct_db())
    # d1.calculate_donations = 100
    # d1.calculate_donations = 10
    # d1.calculate_donations = 50
    # assert d1.fullname == "Billy Galloway"
    # assert d1.donation_total == 160
    # print(repr(d1))
    # donors_ = (d1.fullname, d1.donation_total, d1.times_donated, d1.average_donation)
    # print(donors_)
    # d2 = d("billy")
    # d3 = d("gina")
def test_database():
    pass
    