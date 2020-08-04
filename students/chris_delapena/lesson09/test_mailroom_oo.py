# Chris Dela Pena
# test_mailroom_oo.py

from cli_main import *
from donor_models import *

def test_add_donor():
    entry = Donor("Tim Cook", [100, 900])
    assert entry.donor = "Tim Cook"

def test_donation():
    entry = Donor("Tim Cook", [100, 900])
    assert entry.donations = [100, 900]

def test_num_donations():
    entry = Donor("Tim Cook", [100, 900])
    assert entry.num_donations == 2

def test_sum_donations():
    entry = Donor("Tim Cook", [100, 900])
    assert entry.sum_donations == 1000

def test_thank_you():
    entry = Donor("Tim Cook", [100, 900])
    letter = ('Dear Tim Cook, thank you for your generous donation of $1000. Regards, the Club Owners')
    assert entry.print_thank_you() == letter
