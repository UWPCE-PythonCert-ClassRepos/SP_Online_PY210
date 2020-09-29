import pytest
import numpy as np
from mailroom_oo import Donor, DonorCollection

def testDonor_init():
    d1 = Donor('henry',50)
    assert d1.name == 'henry'
    assert d1.donation == 50

def testDonor_sort():
    d1 = Donor('henry',[50,90])
    d2 = Donor('george',[1000,3000])
    d3 = [d1,d2]
    d3.sort(reverse=True)
    assert d3[0].name == 'george'

def test_totalDonated():
    d1 = Donor('henry',[50,90])
    assert d1.total_donated == 140

def test_totalDonated():
    d1 = Donor('henry',[50,90])
    assert d1.avg_donation == 70

def test_numDonations():
    d1 = Donor('henry',[50,90])
    assert d1.num_donations == 2

def test_DonorCollection_init():
    d2 = DonorCollection()
    assert d2.donors == []

def test_DonorCollection_addDonor():
    d2 = DonorCollection()
    d2.add_donor('jaques',[90,20])
    assert d2.donors[0].name == 'jaques'
    assert d2.donors[0].donation == [90,20]

def test_DonorCollection_addDonation():
    d2 = DonorCollection()
    d2.add_donor('jaques',[90,20])
    d2.add_donation('hilda',[1000,20000])
    assert d2.donors[1].name == 'hilda'
    assert d2.donors[1].donation == [1000,20000]

def 