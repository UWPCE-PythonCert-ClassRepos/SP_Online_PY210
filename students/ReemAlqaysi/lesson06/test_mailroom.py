#!/usr/bin/env python3
import pytest
from mailroom import *
import os

# check if we are getting the right text with the right donor and donation amounts
def test_thank_you_text():
    fullname = 'Reem Alqaysi'
    amount = 222
    letter = "\n\nDear Reem Alqaysi:\n Thank you for your donation of $222, we appriciate your support to our service. \n MailRoom Team\n"
    try:
        assert thank_you_text(fullname,amount) == letter
    except AssertionError:
        print ('we have a problem.')

#test adding new donor to the list
def test_new_donor():
    add_name('Reem Alqaysi')
    try:
        assert 'Reem Alqaysi' in donor_list
    except AssertionError:
        print ('we have a problem.')

    
#test update a donor
def test_update_donor():
   fullname = 'Rabi Das'
   add_name(fullname)
   assert fullname in donor_list

#test report math result
def test_create_report():
    report = [('Scott Newman', 5100.0, 2, 2550),
              ('Joe McHennry', 3000.0, 2, 1500),
              ('Rabi Das', 1450.0, 2, 725),
              ('Jeff Hansen', 902.0, 3, 301), 
              ('Jan Balard', 850.0, 2, 425)
              ]
    assert create_report() == report

#test add amount to a name
def test_add_amount():
    fullname = 'Rabi Das'
    amount = 222
    add_amount(fullname,amount)
    assert donor_list[fullname][-1] == amount

#test is report file exist in directory
def test_create_report_file():
    letter_to_all()
    for name in donor_list:
        filename = name.replace(' ', '_') + ".txt"
        filename = filename.lower()
        assert os.path.isfile(filename) is True