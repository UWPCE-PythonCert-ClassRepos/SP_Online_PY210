#Test Mailroom

from donor_models import*
from cli_main import *

def test_donor_name():
    d1 = Donor("John", [150080.00, 41.28])
    assert d1.name == "John"

def test_add_donation():
    d1 = Donor("John", [150080.00, 41.28])
    d1.add_donation(677)
    assert d1.donations == [150080.00, 41.28, 677]

def test_donor_donations():
    d1 = Donor("John", [150080.00, 41.28])
    assert d1.donations == [150080.00, 41.28]

def test_donation_math():
    d = Donor('Jessica')
    d.add_donation(300.0, 100)
    assert d.total_donation == 400.0
    assert d.num_donations == 2
    assert d.avg_donation == 200

def test_thank_you_mail():
    d1 = Donor("Lilly", [200])
    expected = ('Thank you Lilly, for your generous donation of $200.00 !')
    assert d1.thank_you_mail() == expected

def test_add_donor():
    name = "Jessica"
    donation = 600
    d1 = Donor(name, [donation])
    data.add_donor(name, donation)
    assert name in data._data.keys()
