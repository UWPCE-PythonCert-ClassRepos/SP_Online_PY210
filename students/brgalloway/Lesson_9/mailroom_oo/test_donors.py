import pytest
from mailroom_oo.donor_models import Donor as d


def test_donors():
    d1 = d("Billy Galloway", 100)
    assert d1.fullname == "Billy Galloway"
    assert d1.donation_total == 100
    
   
    print(repr(d1))
    print(d1.average_donation)