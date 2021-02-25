#!/usr/bin/env python3
"""
Created on Mon Jan 11 21:40:03 2021

@author: johnh
"""

#Mailclassroom test

import pytest
import donor_models
import cli_main

import sys
import pathlib
from operator import itemgetter

# Tests for the base class
def test_donor():
    pass#pass in valid inputs, get returns of valid outputs, handle invalid data passing attempts
    
def test_donor_amount():
    #get a list of donors, use them as keys, for each key return a list with only numeric values
    amount = donor_models.Donor()#get the list of donations, sum it and compare it to the saved value for all donors
    assert sum(amount[:]) == total 
    
def test_donor_name():
    #get list of donor names, validate first and last construction
    names = list_of_names
    #for loop through all names to make sure both the first and last are there and nonnumeric strings
    has_first = []
    has_last = []
    
def test_donor_email():
    #from the view email(as opposed to saving in a file), confirm the structure of the email for one donor
    get_first = None
    get_last = None
    full_name = get_first + " " + get_last
    email_piece = donor_models.Donor()
    assert email_piece.return_email ==\
    f"Dear {full_name.title()},\n\n"
    f"Thank you for your generous donation(s) of ${total:,d}.\n"
    "\n"
    "Sincerly,\n"
    "John Hunter\n"
    
# Tests for the subclass Data, for which Donor is the super class
def test_data():
    pass#pass in valid inputs, get returns of valid outputs, handle invalid data passing attempts

def test_get_total():
    #for any donor, the list should be of non zero length, only have numeric data which is summable
    total_validation = donor_models.Data()
    assert len(data_dict[key][0]) != 0
    for key in data_dict:
        for i in data_dict[key][0]:
            assert not i.isnumeric
    assert total_validation.get_total == data_dict[key][1]#reformulates the total and compares it against the stored value
    
def test_extend():
    # for the types offered, the addition of address(dict), phone number(str), activity date, status.
    # need to pass in a valid value of the type, keep a dictionary of the order in which these have been added
    extending = donor_models.Data()
    extending.extend(extended_dict[value]) = sample_value
    #then once the module adds the empty value to all other donor entries
    for key in data_dict:
        assert data_dict[key][extended_dict[value]] == (None or sample_value)
    
def test_construct_email():#add more, gift receipt, return address, calendar date of last donation 
    email_piece = donor_models.Data()
    assert email_piece.return_email ==\
    f"Dear {full_name.title()},\n\n"
    f"Thank you for your generous donation(s) of ${total:,d}.\n"
    "\n"
    "Sincerly,\n"
    "John Hunter\n"

def test_sort_key_data():
    # use mock data, mock up new users and sort by predictable data ordering donations totals only
    other_sort = donor_module.Data()
    assert sorted == expected
    
# Tests for the Report subclass, this is subclassed from Data
def test_report():
    #pass in valid inputs, get returns of valid outputs, handle invalid data passing attempts
    # validate sizes of the largest objects and the field sizes
    pass
    
def test_header():
    # header is exact match and adjustable based on extension of data
    # creates header based on the data extended fields
    assert header_object == expected
    
def test_report_data():
    pass#organizes but does not print the data, confirms formatting based on size of all included data

def test_sort_key_report():
    # use mock data, mock up new users and sort by predictable data ordering
    other_sort = donor_module.Data()
    assert sorted == expected
#Tests for the Interface
def test_interface():
    pass#pass in valid inputs, get returns of valid outputs, handle invalid data passing attempts

def test_select_read_in():
    pass# can accept valid data, handles invalid input, returns per expectations
    for i in choices:#pass in a list that has many options for input data
        bad_data = function(i)
        assert bad_data is False
    assert good_data is True
    
def test_menu():
    # can accept valid data, handles invalid input, returns per expectations
    # can call all functions
    pass

def test_choice_add_donor():
    # can accept valid data, handles invalid input, returns per expectations
    # can call all functions
    pass
    
def test_choice_add_donation():
    # can accept valid data, handles invalid input, returns per expectations
    # can call all functions
    pass

def test_choice_reademail_readreport():
    # can accept valid data, handles invalid input, returns per expectations
    # can call all functions
    pass

def test_choice_extend():
    # can accept valid data, handles invalid input, returns per expectations
    # can call all functions
    pass
    
#Tests for the Read class
def test_read():
    pass#pass in valid inputs, get returns of valid outputs, handle invalid data passing attempts

def test_read_in_donors():
    pass# can accept valid data, handles invalid input, returns per expectations

def test_read_in_data():
    pass# can accept valid data, handles invalid input, returns per expectations

def test_read_in_all():
    pass# can accept valid data, handles invalid input, returns per expectations

def test_save_emails():
    pass# can accept valid data, handles invalid input, returns per expectations

def test_save_report():
    pass# can accept valid data, handles invalid input, returns per expectations


