import pytest
from mailroom import *
from cli_main import *
from os import listdir
import numpy as np
#----------------Test Donor class-----------------------------
def test_Donor():
    #Tests creation of donor
    test_name = 'John Smith'
    test_donations = [1,2,3]
    d = Donor(test_name,test_donations)
    assert d.name == test_name
    assert d.donations == test_donations
    try:
        Donor('Bobby B',5)
        assert False
    except TypeError:
        assert True

def test_add_donation():
    #Tests donation added to Donor
    test_name = 'John Smith'
    test_donations = [1, 2, 3]
    d = Donor(test_name, test_donations)
    add_on = 5
    assert d.add_donation(add_on) == test_donations.append(add_on)

def test_calculate_report():
    #Tests report info calculated for donor
    test_name = 'John Smith'
    test_donations = [1, 2, 3]
    d = Donor(test_name, test_donations)
    tot, num, av = d.calculate_report()
    assert tot == sum(test_donations)
    assert num == len(test_donations)
    assert av == np.mean(test_donations)

def test_form_report():
    # Test form_report
    donors = [D('Luke Skywalker',[10,20,30]),D('Leslie Knope',[100,300]),D('Dwight Schrute',[345,345345]),D('Freddie Mercury',[23532,32]),D('Jennifer Aniston',[235,2352])]
    dc = DonorCollection()
    for person in donors:
        dc.add_donor(person)
    name_lst_sorted, donor_report = dc.form_report()
    assert name_lst_sorted == ['Dwight Schrute','Freddie Mercury','Jennifer Aniston','Leslie Knope','Luke Skywalker']


#----------------Test DonorCollection class-------------------
def test_DonorCollection():
    #Tests collection creation
    dc = DonorCollection()
    assert dc.donor_list == []
    test_name = 'John Smith'
    test_donations = [1, 2, 3]
    d = Donor(test_name, test_donations)
    dc.add_donor(d)
    assert dc.donor_list == [d]

def test_add_to_list():
    #Tests add donation to existing
    dc = DonorCollection()
    test_name = 'John Smith'
    test_donations = [1, 2, 3]
    d = Donor(test_name, test_donations)
    dc.add_donor(d)

    new_donation = 4
    dc.add_to_list(test_name,new_donation)
    assert d.donations == test_donations

    #Tests add new donor
    test_name2 = 'Jane Doe'
    test_donations2 = 4
    dc.add_to_list(test_name2,test_donations2)
    assert dc.donor_list[1].name == test_name2

def test_print_donors():
    #Tests donor list printed
    dc = DonorCollection()
    test_name = 'John Smith'
    test_donations = [1, 2, 3]
    d = Donor(test_name, test_donations)
    dc.add_donor(d)
    test_name2 = 'Jane Doe'
    test_donations2 = 4
    dc.add_to_list(test_name2, test_donations2)
    assert dc.print_donors() == 'John Smith\nJane Doe\n'

#----------------Test Command Line Interface------------------
def test_exit():
    # Test 'exit'
    dc = DonorCollection()
    assert give_thanks(dc,'exit') == None

def test_created_files():
    # Working (files exist)
    dc = DonorCollection()
    assert dc.donor_list == []
    test_name = 'John Smith'
    test_donations = [1, 2, 3]
    d = Donor(test_name, test_donations)
    dc.add_donor(d)
    directory = 'C:\_PythonCLass\Python210_working\session09\practice_folder' #Will need to change this to a file on your computer
    many_thanks(dc,directory)
    filenames = listdir(directory)
    assert 'JohnSmith.txt' in filenames

#Test thank_you_text
def test_thank_you():
    donor = 'Chucky Cheese'
    assert thank_you_text(donor) == f'Dear {donor}, \n Thank you for your generous donation. We appreciate the support from people like you. \n Thank you,\n Charity Name'