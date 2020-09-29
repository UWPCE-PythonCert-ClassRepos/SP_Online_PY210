import pytest
from donor_models import Donor
from donor_models import DonorCollection as Donors
import pathlib

"""
test_donor_models.py: test module
lesson 9
joli umetsu
python210
"""

#--- Tests for Donor class ---

def test_Donor_new():
    """ tests whether a donor object can be created """
    donor = Donor("Gimli", [90030,20000])
    assert donor.name == "Gimli"
    assert donor.donations == [90030,20000]
    
def test_Donor_add():
    """ tests that a donation can be added for a donor """
    donor = Donor("Gimli", [90030,20000])
    donor.add_donation(5000)
    assert donor.donations == [90030,20000,5000]
    
def test_Donor_total():
    """ tests calculation of a donor's total donations """
    donor = Donor("Gimli", [90030,20000,5000])
    assert donor.donation_total == 115030
    
def test_Donor_number():
    """ tests calculation of a donor's number of donations """
    donor = Donor("Gimli", [90030,20000,5000])
    assert donor.donation_number == 3
    
def test_Donor_average():
    """ tests calculation of a donor's average donation """
    donor = Donor("Gimli", [90030,20000,5000])
    assert donor.donation_average == 38343.33
    
def test_Donor_letter():
    """ tests that donor letter text is generated """
    donor = Donor("Gimli", [90030,20000,5000])
    note = donor.letter()
    assert note.startswith("Dear Gimli")
    assert "donations totaling $115030.00" in note


#--- Tests for DonorCollection class ---

def test_DonorCollect_list():
    """ tests string that lists existing donor names """
    donors = Donors()
    assert donors.list_donors().startswith("\nPeregrin Took")
    assert donors.list_donors().endswith("Frodo Baggins\n")
    
def test_DonorCollect_search():
    """ tests that search by name returns list with name if exists """
    donors = Donors()
    find = donors.search_donor("Smeagol")
    assert "Smeagol" in find
    
def test_DonorCollect_add():
    """ tests whether a new donor can be added """
    donors = Donors()
    donors.add_donor("Gimli",[90,20])
    find = donors.search_donor("Gimli")
    assert "Gimli" in find
    
def test_DonorCollect_update():
    """ tests whether an existing donor's information can be updated """
    donors = Donors()
    donor = donors.update_donor("Smeagol", 500)
    n = donor.donation_number
    assert n == 2
    
def test_DonorCollect_report():
    """ tests whether report list is being generated and sorted """
    donors = Donors()
    report = donors.report()
    assert report[0] == ["Samwise Gamgee", 10601.93, 3, 3533.98]
    assert report[4] == ["Smeagol", 45.01, 1, 45.01]

def test_DonorCollect_letters():
    """ tests if letters are generated with correct content """
    donors = Donors()
    donors.letters()
    d = pathlib.Path('.').absolute()
    p = d / 'ThankYouLetters'
    f1 = "Peregrin_Took.txt"
    f2 = "Smeagol.txt"
    f3 = "Samwise_Gamgee.txt"
    assert p/f1 in p.iterdir()
    assert p/f2 in p.iterdir()
    assert p/f3 in p.iterdir()
    with open( p/f2, 'r' ) as f:
        content = f.read()
    assert content.startswith("Dear Smeagol,")
    
    
    