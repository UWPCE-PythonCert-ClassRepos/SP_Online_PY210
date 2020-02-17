# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:18:10 2020

@author: Grant Dowell
Assignment 5 - Unit Tests of Mailroom Part 4
"""
import mailroom_part4
from mailroom_part4 import *
import pytest
import os

mailroom_part4.db = {"bill": [2.00],
                     "joe": [1.00, 2.00]}

def test_generate_letter():    
    expect = "Dear Joe,\n\n" + \
               "Thank you for your most recent donation of " + \
               "$2.00. We greatly appreciate it.\n\n" + \
               " ~ The Treasurer"
    name = 'joe'
    assert generate_letter(name) == expect
    
def test_report():
    expect = "Donor Name            | Total Given | Num Gifts | Average Gift\n" + \
             "--------------------------------------------------------------\n" + \
             "Joe                    $       3.00           2  $        1.50\n" +\
             "Bill                   $       2.00           1  $        2.00\n"
    assert report() == expect
    
def test_log_all_letters():
    log_all_letters()
    assert os.path.exists('joe.txt')
    
def test_add_donor():
    expect_keys = ['bill', 'joe', 'fred']
    add_donor('Fred')
    assert type(mailroom_part4.db['fred']) is list
    assert all(name in mailroom_part4.db for name in expect_keys)
    
def test_add_donation():
    expect_db = {'joe': [1.00, 2.00, 3.00], 'bill':[2.00]}
    add_donation('joe', 3.00)
    for key in expect_db:
        assert mailroom_part4.db[key] == expect_db[key]
    