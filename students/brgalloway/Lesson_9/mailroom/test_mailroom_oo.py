import pytest
from donor_models import *

def test_donors():
    d1 = Donor("Billy Galloway")
    d1.donate = 100
    d1.donate = 10
    d1.donate = 50
    assert d1.fullname == "Billy Galloway"
    assert d1.donation_total == 160
    print(d1)

def test_database():
    d1 = Donor("Billy")
    d2 = Donor("Gina")
    db = DonorCollection()

    db.append(d1)
    db.append(d2)
    d2.donate = 100
    d2.donate = 100
    assert db.donor_list[1].fullname == "Gina"
    db.search("Roger")
    print(db.generate_report())


    