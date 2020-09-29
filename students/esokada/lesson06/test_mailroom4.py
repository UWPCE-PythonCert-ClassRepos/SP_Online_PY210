'''
Unit tests for the mailroom assignment (part 4).
'''

import pytest

from mailroom4 import *

import os

#donors dictionary for use with tests

donors = {
          "Poirot":[13.2, 14.12, 120.1],
          "Hastings":[13, 440, 1213],
          "Inspector Japp":[670.1, 50],
          "Miss Lemon": [423, 23.7]
          }

#tests for functions used in send_thankyou()

def test_show_donorlist():
    expected = ['Poirot', 'Hastings', 'Inspector Japp', 'Miss Lemon']
    assert show_donorlist(donors) == expected

def test_add_donor():
    donorname = "Miss Marple"
    add_donor(donorname, donors)
    assert "Miss Marple" in donors
    #prevent issues with Miss Marple having no donations in subsequent tests
    update_donor("Miss Marple", donors, 456)

def test_update_donor():
    donorname = "Poirot"
    amount = 1234
    update_donor(donorname, donors, amount)
    assert 1234 in donors["Poirot"]

def test_write_oneletter():
    donorname = "Roderick Allyn"
    amount = 345
    letter = write_oneletter(donorname, amount)
    assert "Roderick Allyn" in letter
    assert "generous donation" in letter
    assert "345" in letter

#test for functions used in write_report()

def test_create_rows():
    testreport = create_rows(donors)
    assert testreport.startswith("Donor")
    assert "Poirot" in testreport
    assert "1666" in testreport

#tests for functions used in batch_letters()

def test_batch_letters_text():
    k = "Usagi"
    v = [1, 2, 3]
    sample_letter = batch_letters_text(k, v)
    assert "Usagi" in sample_letter
    assert "3.00" in sample_letter
    assert "6.00" in sample_letter

def test_batch_letters_files():
    for k, v in donors.items():
        filetext = batch_letters_text(k, v)
        batch_letters_files(k, filetext)
        assert os.path.isfile("Poirot.txt") is True
