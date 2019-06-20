import pytest, os
from donor_models import *
import donor_models as d

def test_donors():
    d1 = Donor("Billy Galloway", [100, 1, 100])
    assert d1.fullname == "Billy Galloway"
    assert d1.donation_total == [100, 1, 100]
    assert d1.sum_of_donations == 201
    assert d1.times_donated == 3

    print(repr(d1))

def test_database():
    db = DonorCollection(Donor("Billy", [100, 1, 100]))
    print(db.donor_list)
    db.add_donations()
    
    # db = DonorCollection()
    # db.append(d1)
    # db.append(d2)
    # d2.donate = 100
    # d2.donate = 100
    # assert db.donor_list[1].times_donated == 2
    # assert db.donor_list[1].fullname == "Gina"
    # assert db.donor_list[1].donation_total == 200
    # assert db.donor_list[1].average_donation == 100

# def test_send_thankyou():
#     email_template = Donor.send_thankyou(Donor, "Paul Allen", 10)
#     with open("Paul_Allen.txt", "r") as file:
#         email_output = file.readlines()
#     assert os.path.isfile("Paul_Allen.txt") == True
#     email_template = Donor.send_thankyou(Donor, "Larry David", 10)
#     with open("Larry_David.txt", "r") as file:
#         email_output = file.readlines()

#     assert os.path.isfile("Larry_David.txt") == True

# def test_bulk_email():
#     d1 = Donor("Billy")
#     d2 = Donor("Gina")
#     db = DonorCollection()
#     db.append(d1)
#     db.append(d2)
#     d2.donate = 100
#     d2.donate = 100
    
#     email_output = DonorCollection.bulk_thankyou(DonorCollection, db.donor_list)
#     assert os.path.isfile("Billy.txt") == True
#     assert os.path.isfile("Gina.txt") == True
