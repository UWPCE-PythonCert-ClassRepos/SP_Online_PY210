import pytest, os
from donor_models import *
import donor_models as d

def test_donors():
    d1 = Donor("Billy Galloway", 100)
    assert d1.fullname == "Billy Galloway"
    assert d1.donation_total == [100]
    d1.apply_donation(1)
    d1.apply_donation(100)
    assert d1.donation_total == [100, 1, 100]
    assert d1.sum_of_donations == 201
    assert d1.times_donated == 3
    print(d1.fullname)

def test_database():
    db = DonorCollection(Donor("Billy Galloway", [100, 1, 100]))
    db.generate_report()
    db.apply_donation("Billy Galloway", 10)
    db.bulk_thankyou()
    assert os.path.isfile("Billy_Galloway.txt") == True
    assert db.donor_list["Billy Galloway"].times_donated == 4
    db.generate_report()



