#!/usr/bin/env python

from donor_models import Donor
from donor_models import DonorCollection
import os.path
import pathlib
import pytest

donor = DonorCollection()


def test_donors_history():
    """ Test donor in the History of dictionary of donors created """
    donor = Donor('Jeff Bezos')
    assert donor.name == 'Jeff Bezos'
     

def test_donors_list():
    """ Test all donor names are returned"""
     
    donor.add(Donor('ABC', [1001.00]))
    donor.add(Donor('Indu', [400.00]))
    assert 'ABC' in donor.donors_list()
    assert 'Indu' in donor.donors_list()
    assert 'ABC\nIndu' in donor.donors_list()

def test_donation_update():
    donor = Donor('Indu', [90.00])
    assert len(donor.donation_amt) == 1
    assert sum(donor.donation_amt) == 90.00
    
  
def test_thankyou_note():
    """ Test  Thank you Note """
    donor = Donor('Jeff Bezos', [877.33])
    assert '877.33' in donor.print_thanksnote()

def test_send_letters():

    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath,'Mark Zuckerberg.txt')
    file2 = os.path.join(dirpath, 'Paul Allen.txt')
    donor.send_letters_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)


