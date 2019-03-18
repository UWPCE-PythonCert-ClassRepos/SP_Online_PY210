"""
test code for mailroom_fp.py
"""

import pytest
import datetime
import os.path
import pathlib

from mailroom_fp import *

def test_donor_name():
    d = Donor("Jack Bogle")
    assert d.name == "Jack Bogle"
    
def test_total_donation():
    d = Donor("Jack Bogle")
    d.add_donation(50)
    d.add_donation(100)
    d.add_donation(200)
    d.add_donation(25)
    d.add_donation(25)
    assert d.total_donation() == 400

def test_num_donation():
    d = Donor("Jack Bogle")
    d.add_donation(50)
    d.add_donation(100)
    d.add_donation(200)
    d.add_donation(25)
    d.add_donation(25)
    assert d.num_donation() == 5

def test_avg_donation():
    d = Donor("Jack Bogle")
    d.add_donation(50)
    d.add_donation(100)
    d.add_donation(200)
    d.add_donation(25)
    d.add_donation(25)
    assert d.avg_donation() == 80

def test_collection():
    d1 = Donor("Jack Bogle")
    d1.add_donation(50)
    d2 = Donor("Sam Smith")
    d2.add_donation(100)
    d2.add_donation(150)
    d3 = Donor("Jack Ma")
    d3.add_donation(200)
    donor_collection = DonorCollection()
    donor_collection.add_donor(d1)
    donor_collection.add_donor(d2)
    donor_collection.add_donor(d3)
    assert donor_collection.donor_names() == ["Jack Bogle", "Sam Smith", "Jack Ma"]
    
def test_write_letter():
    donor_collection = initial_setup()
    donor_collection.write_letter()
    
    current = datetime.datetime.now()
    abs_path = pathlib.Path('./').absolute()
    final_path = os.path.join(abs_path, "letter_storage/")
    
    assert "Orville Wright_{:02}_{:02}_{:02}.txt".format(current.month, current.day, current.year) in os.listdir("letter_storage")
    assert "Warren Buffett_{:02}_{:02}_{:02}.txt".format(current.month, current.day, current.year) in os.listdir("letter_storage")
    assert "Jack Bogle_{:02}_{:02}_{:02}.txt".format(current.month, current.day, current.year) in os.listdir("letter_storage")
    
def test_challenge():
    d1 = Donor("Jack Bogle")
    d1.add_donation(50)
    d2 = Donor("Sam Smith")
    d2.add_donation(100)
    d2.add_donation(150)
    d3 = Donor("Jack Ma")
    d3.add_donation(200)
    donor_collection = DonorCollection()
    donor_collection.add_donor(d1)
    donor_collection.add_donor(d2)
    donor_collection.add_donor(d3)
    assert donor_collection.challenge(2, 60, 190) == 250
    assert donor_collection.challenge(3, 0, 210) == 1000