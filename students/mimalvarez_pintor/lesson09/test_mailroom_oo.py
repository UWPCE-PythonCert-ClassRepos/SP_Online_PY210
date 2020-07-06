# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:02:03 2020

@author: miriam
"""

from donor_models import Donor
from donor_models import DonorCollection
import os.path
import pathlib
import pytest

donor = DonorCollection()


def test_donors_history():
    """ Test donor in the History of dictionary of donors created """
    donor = Donor('Urias Gramajo')
    assert donor.name == 'Urias Gramajo'


def test_donors_list():
    """ Test all donor names are returned"""
    donor.add(Donor('Noe', [50]))
    donor.add(Donor('David', [500]))
    assert 'Noe' in donor.donors_list()
    assert 'David' in donor.donors_list()
    assert 'Noe\nDavid' in donor.donors_list()


def test_donation_update():
    donor = Donor('David', [90])
    assert len(donor.donation_amt) == 1
    assert sum(donor.donation_amt) == 90.00


def test_thankyou_note():
    """ Test  Thank you Note """
    donor = Donor('Urias Gramajo', [1000.00])
    assert '1000.00' in donor.print_thanksnote()


def test_send_letters():
    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath, 'Urias Gramajo.txt')
    file2 = os.path.join(dirpath, 'Miriam Pintor.txt')
    donor.send_letters_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)