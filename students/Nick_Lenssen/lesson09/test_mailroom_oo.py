
import io
import pytest
from donor_models import *

from donor_models import Donor
from donor_models import DonorCollection


def test_create_donor():
    d = Donor('Mike Jones')
    assert d.name == 'Mike Jones'

def test_donation_math():
    d = Donor('Mike Jones')
    d.add_donation(200.0,100)
    assert d.total_donation == 300.0
    assert d.num_donation == 2
    assert d.ave_donation == 150

def test_compare_donors():
    d1, d2 = Donor('Nick F'), Donor('Stephen S')
    d1.add_donation(200.0)
    d1.add_donation(300.0)
    d2.add_donation(650.0)
    assert d1 < d2

def test_create_donor_collection():
    dc = DonorCollection()
    assert isinstance(dc, DonorCollection)

def test_add_donor_to_collection():
    d1, d2 = Donor('Nick F'), Donor('Nick L')
    dt = DonorCollection()
    dt.add_donors(d1, d2)
    #fails but does what I want, [Nick F, Nick L] != ['Nick F', 'Nick L']
    assert dt.list_donors == [d1.name, d2.name]













