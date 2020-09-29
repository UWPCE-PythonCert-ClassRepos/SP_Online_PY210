#!/usr/bin/env python

from donor_models import Donor
from donor_models import DonorCollection
import os.path
import pathlib
import pytest

donor = DonorCollection()


def test_donors_history():
    """ Test donor name in the donor dictionary created """
    donor = Donor('Anton Chekhov')
    assert donor.name == 'Anton Chekhov'
     

def test_donors_list():
    """ Test all donor names are returned"""
     
    donor.add(Donor('Mikhail Bulgakov', [800.00]))
    donor.add(Donor('Ivan Turgenev', [400.00]))
    assert 'Mikhail Bulgakov' in donor.list_of_donors()
    assert 'Ivan Turgenev' in donor.list_of_donors()
    assert 'Mikhail Bulgakov\nIvan Turgenev' in donor.list_of_donors()

def test_donation_update():
    donor = Donor('Ivan Turgenev', [150.00])
    assert len(donor.donation_amt) == 1
    assert sum(donor.donation_amt) == 150.00
    
  
def test_thankyou_note():
    """ Test  Thank you Note """
    donor = Donor('Anton Chekhov', [741.99])
    assert '741.99' in donor.print_thank_you_message()

def test_send_letters():

    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath,'Mikhail Lermontov.txt')
    file2 = os.path.join(dirpath, 'Alexander Pushkin.txt')
    donor.send_letters_to_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)
