#!/usr/bin/env python
import os.path

from mailroom_Part_4 import list_donor
from mailroom_Part_4 import donorlist
from mailroom_Part_4 import donor_addition
from mailroom_Part_4 import decode_input
from mailroom_Part_4 import lettersToAllDonors
from mailroom_Part_4 import get_letter_text
from mailroom_Part_4 import create_report

#test output of 'list' command
def test_1():
    assert list_donor() == donorlist.keys()

#returns 1 for special case "list" else returns 0
def test_2():
    assert decode_input("list") == 1

#test adding a new donor
def test_3():
    donor_addition("Ajay", 500)
    key, value = "Ajay", [500, 1, 500]
    assert key in donorlist and value == donorlist[key]

#Test updating an existing donor's donation
def test_4():
    donor_addition("Elon Musk", 1000)
    key, value = "Elon Musk", [1500, 3, 500]
    assert key in donorlist and value == donorlist[key]

def test_5():
    assert create_report() is None

def test_6():
    lettersToAllDonors()
    assert os.path.isfile("Elon_Musk.txt")

def test_7():
    expected = "Dear Elon Musk,\n\n    Thank you for your very kind donation of 1500.\n    It will be put to very good use.\n\nSincerely, \n-The Team"
    assert get_letter_text("Elon Musk", 1500) == expected