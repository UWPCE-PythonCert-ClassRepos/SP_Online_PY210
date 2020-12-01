#!/usr/bin/env python
import os.path

from mailroom_Part_4 import list_donor
from mailroom_Part_4 import donorlist
from mailroom_Part_4 import donor_addition
from mailroom_Part_4 import decode_input
from mailroom_Part_4 import letters_ToAllDonors
from mailroom_Part_4 import get_letter_text
from mailroom_Part_4 import create_report
from mailroom_Part_4 import *

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

#test that the list is sorted by total amount in descending order
def test_5():
    prev = []
    for donor, (total, number, average) in create_report():
        prev.append(total)
        print(prev)
    for index in range(len(prev)-1):
        assert prev[index] >= prev[index+1]

def test_6():
    letters_ToAllDonors()
    assert os.path.isfile("Elon_Musk.txt")

def test_7():
    expected = "Dear Elon Musk,\n\n    Thank you for your very kind donation of 1500.\n    It will be put to very good use.\n\nSincerely, \n-The Team"
    assert get_letter_text("Elon Musk", 1500) == expected