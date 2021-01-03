#!/usr/bin/env python
import os.path


from mailroom_oo import *
from donor_models import *


def test1():
    """
    verify the new donor object is created and attributes accessible
    """
    a = Donor("Ajay Randhawa", 500)
    assert a.name == "Ajay Randhawa"
    assert a.donation_count == 1
    assert a.total_donation == 500
    assert a.avg_donation == 500
    assert x == 0

#returns 1 for special case "list" else returns 0
def test2():
    assert decode_input("list") == 1

#Test updating an existing donor's donation
def test4():
    i = DonorCollection(donor_list)
    i.add_donation("Elon Musk", 1000)
    key, value = "Elon Musk", [1500, 3, 500]
    assert key in i.donorlist and value == i.donorlist[key]

#Test to verify the a letter was created
def test5():
    database.letters_toAllDonors()
    assert os.path.isfile("Elon_Musk.txt")

def test6():
    """
    verify the thankyou message prints correct name and donation
    """
    b = Donor("Ajay Randhawa", 500)
    file_contents = b.send_thankyou('Ajay Randhawa', 500)

def test7():
    '''
    Verify the addition of additional donations is saved correctly and accesible
    '''
    c = Donor("Ajay Randhawa", 500)
    c.add_donation("Ajay Randhawa", 1000)
    assert c.donation_count == 2
    assert c.total_donation == 1500
    assert c.avg_donation == 750

def test8():
    '''
    verifies the input dict for the DonorCollection class correctly parses data
    '''
    d = DonorCollection(donor_list)
    file_contents = d.donorlist 
    assert "Elon Musk" in file_contents
    assert 'Mark Zuckerburg' in file_contents
    assert "William Gates" in file_contents
    for donor, donations in file_contents.items():
        if donor == "William Gates":
            assert donations[0] == 150
            assert donations[1] == 2
            assert donations[2] == 75
    
def test9():
    '''
    Tests that a donor instance is saved in a list named instance
    tests that additional donations by a donor are added to the same instance
    '''
    e = DonorCollection(donor_list)
    print(len(e.donorlist))
    print(len(e.instance))
    e.add_donation("Nathan Adamson", 50)
    print(len(e.instance))
    print(e.instance[5].total_donation)
    assert e.instance[5].name == "Nathan Adamson"
    assert e.instance[5].total_donation == 50
    e.add_donation("Nathan Adamson", 100)
    print(len(e.instance))
    assert e.instance[5].name == "Nathan Adamson"
    assert e.instance[5].total_donation == 150

def test10():
    '''
    Verify an input of 'list' outputs the correct response
    '''
    f = DonorCollection(donor_list)
    assert (decode_input("list")) == 1

def test11():
    '''
    test to verify the sort method
    '''
    g = DonorCollection(donor_list)
    list1 = g.sort_list(donor_list)
    print(list1)
    index = []
    for donor, [total, count, avg] in list1:
        index.append(total)
    assert index[0] >= index[1]
    assert index[1] >= index[2]
    assert index[2] >= index[3]
    
