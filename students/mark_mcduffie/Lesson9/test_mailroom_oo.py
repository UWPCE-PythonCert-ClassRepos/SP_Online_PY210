from donor_models import Donor
from donor_models import DonorCollection

donor = DonorCollection()

def test_original():
    donor = Donor('Jim Johnson', 50.00)
    assert donor.name == 'Jim Johnson'


def test_add():
    donor.add_donor(Donor('Mark McDuffie', 20.00))
    donor.add_donor(Donor('Bill Gates', 40000.00))
    assert 'Mark McDuffie' in donor.donor_list()
    assert 'Bill Gates' in donor.donor_list()


def test_donations():
    donor = Donor('X', [20.00, 10.00])
    assert len(donor.donation) == 2
    assert sum(donor.donation) == 30.00

