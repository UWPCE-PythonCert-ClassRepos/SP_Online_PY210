import pytest
from donor_models import Donor, DonorCollection
import os
import time

def test_create_donor():
    d = Donor('Sue')
    assert d.name == 'Sue'

def test_math():
    d = Donor('Karen')
    d.add_donation(4,2)
    assert d.d_tot == 6
    assert d.d_num == 2
    assert d.d_avg == 3

def test_thanks_all():
    tdc = DonorCollection()
    don = Donor('Mo')
    don.add_donation(4,2)
    tdc.add_donors(don)
    tdc.thanks_all()
    parent = os.getcwd()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(parent, timestr + "/" + 'Mo.txt')
    assert os.path.exists(filename)

def test_thanks():
    expected =  (f"""
Dear Larry,

Thank you for your very kind donation of $90.00

It will be put to very good use.

Sincerely,
-The Team""")

    dc = DonorCollection()
    r1 = 'Larry'
    donor_new = Donor(r1)
    dc.add_donors(donor_new)
    donor1 = donor_new
    donor1.add_donation(40,50)
    assert donor1.send_thank_you(donor1.d_tot) == expected


def test_donor_collection():
    dc = DonorCollection()
    assert isinstance(dc, DonorCollection)
