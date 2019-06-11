import pytest
from mailroom_oo.donor_models import Donor as d


def test_donors():
    d1 = d("Billy Galloway")
    assert d1.fullname == "Billy Galloway"
   
    
    
    
    d1.donated = 100
    d1.donated = 100
    d1.donated = 80
    d1.donated = 20
   
   
    print(repr(d1))
    print(d1.average_donation)
    # print(d1.donation_total)
    # d1.donation_total = 100
    # print(d1.donation_total)