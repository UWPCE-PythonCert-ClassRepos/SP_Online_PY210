import pytest
from donor_models import *
from cli_main import *
import os
from os import listdir

def test_Donor_initial():
    name = 'Kobe Bryant'
    donations = [8,24,28]
    d = Donor(name, donations)
    #Verify the name, donations, total, number and average properties are correct
    assert d.name == name
    assert d.donations == donations
    assert d.tot_donations == 60
    assert d.num_donations == 3
    assert d.avg_donation == 20

def test_Donor_new_donation():
    name = 'Kobe Bryant'
    donations = [8,24,28]
    d = Donor(name, donations)
    assert d.name == name
    assert d.donations == donations
    #Verify that adding a new donation updates the properties
    d.new_donation(23)
    assert d.num_donations == 4
    assert d.donations[-1] == 23

def test_DonorCollection_initial_new_donor():
    dc = DonorCollection()
    assert dc.donor_list == []
    name = 'Kobe Bryant'
    donations = [8,24,28]
    d = Donor(name, donations)
    dc.new_donor(d)
    #Test the donor collection for adding a new donor
    assert dc.donor_list == [d]

def test_DonorCollection_new_donation():
    dc = DonorCollection()
    name = 'Kobe Bryant'
    donations = [8,24,28]
    d = Donor(name, donations)
    dc.new_donor(d)
    #Verify that the .donor_list recreates the donor list
    assert dc.donor_list == [d]
    dc.new_donation(name, 23)
    #Verify that the added donation is included
    assert d.donations[-1] == 23

    name = 'Gigi Bryant'
    donations = [243, 968]
    d = Donor(name, donations)
    dc.new_donor(d)
    #Verify that the donor list includes the latest addition
    assert dc.donor_list[-1] == d

def test_DonorCollection_list_donors():
    dc = DonorCollection()
    name = 'Kobe Bryant'
    donations = [8,24,28]
    d = Donor(name, donations)
    dc.new_donor(d)

    name = 'Gigi Bryant'
    donations = [243, 968]
    d = Donor(name, donations)
    dc.new_donor(d)

    #Verify the function that lists donors
    assert dc.list_donors() == 'Kobe Bryant\nGigi Bryant\n'

def test_DonorCollection_ty():
    dc = DonorCollection()
    name = 'Kobe Bryant'
    donations = [8, 24, 28]
    d = Donor(name, donations)
    dc.new_donor(d)

    #Verify thank you text
    assert dc.ty_text(name) == 'Dear Kobe Bryant, We appreciate your generosity in the donation amount of $60.00'

def test_CLI_ty_letters():
    dc = DonorCollection()
    name = 'Kobe Bryant'
    donations = [8,24,28]
    d = Donor(name, donations)
    dc.new_donor(d)

    name = 'Gigi Bryant'
    donations = [243, 968]
    d = Donor(name, donations)
    dc.new_donor(d)

    #Verify that "Send letters to all Donors" creates the appropriate .txt file
    send_letters_to_all_donors(dc)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filenames = listdir(dir_path)
    assert 'Kobe Bryant.txt' in filenames
    assert 'Gigi Bryant.txt' in filenames
