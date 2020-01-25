"""
test code for mailroom_oo
"""
import io
import pytest
import math

from donor_models import *

def test_donor_init():
    donor = Donor('mike')
    assert donor.name == 'mike'
    assert donor.donations == []

    donor = Donor('tim smith',[2, 3.1])
    assert donor.name == 'tim smith'
    assert donor.donations == [2, 3.1]

def test_add_donation():
    donor = Donor('tim smith', [2, 3.1])
    donor.add_donation(45.2) 
    donor.donations == [2 , 3.1, 45.2] 

def test_sum_donation():
    donor = Donor('tim smith', [2, 3.1]) 
    assert donor.sum_donation() == 2 + 3.1  

def test_num_donation():
    donor = Donor('tim smith', [2, 3.1]) 
    assert donor.num_donation() == 2  

def test_average_donation():
    donor = Donor('tim smith', [2, 3.1]) 
    assert donor.average_donation() == (2 + 3.1)/2 

def test___lt__():
    a = Donor('mike', [10])
    b = Donor('joe', [20])
    assert a < b 

def test___str__():
    donor = Donor('Mike', [25])
    assert donor.__str__() ==  'Mike                       $      25.00           1  $       25.00'

def test_letter_file_name():
    donor = Donor('Mike Jones', [25])
    assert donor.letter_file_name() == 'Mike_Jones.txt'

def test_DonorCollection_init():
    dc = DonorCollection()
    assert dc.donors == []

def test_sort():
    dc = DonorCollection()
    dc.add_donor(Donor('mike',[20]))
    dc.add_donor(Donor('tim',[40]))
    dc.add_donor(Donor('joe',[30]))
    dc.sort()
    assert dc.donors[0].name == 'tim'
    assert dc.donors[1].name == 'joe'
    assert dc.donors[2].name == 'mike'

def test_add_to_list():
    dc = DonorCollection()
    dc.add_donor(Donor('mike',[20]))
    dc.add_to_list('mike', 30)
    assert dc.donors[0].donations == [20, 30]
    dc.add_to_list('joe', 40)
    assert dc.donors[1].name == 'joe'
    assert dc.donors[1].donations == [40]