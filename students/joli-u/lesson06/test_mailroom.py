#!/usr/bin/env python

import mailroom4 as mail
import copy 
import os 

"""
test code for mailroom part 4
lesson 6
joli umetsu
py210
"""

# dictionary of donors and donation amounts that will be used in some tests 
dict = {
    'Name1' : [5.10,10.10],
    'Name2' : [100.01,100.01],
    }

# ----- TEST: SEND THANK YOUS -----
def test_list_donors():  # checks list of donors shown
    expected_list = print("Name1\nName2")
    assert mail.list_donors(dict) == expected_list

def test_email():  # checks that thank you email text is generated correctly
    name = 'Batman'
    amount = 20.05
    brdr = "-"*55
    body = "\n".join(("Dear Batman,\n", 
        "\tThank you for your generous donation of $20.05.\n", 
        "\tIt will be put to very good use.\n",
        "\t\tSincerely,",
        "\t\t  -The Team"))
    expected_text = print("\n".join((brdr,body,brdr))) 
    assert mail.email(name,amount) == expected_text

def test1_update_donors():  # checks that donor list is updated properly if donor exists
    name = 'Name2'
    amount = 20.08
    test_dict = copy.deepcopy(dict)
    exp_dict = copy.deepcopy(dict)
    exp_dict[name].append(amount)
    mail.update_donors(name,amount,test_dict)
    assert test_dict == exp_dict
    
def test1_update_donors():  # checks that donor list is updated properly if donor doesnt exist
    name = 'Name3'
    amount = 100.10
    test_dict = copy.deepcopy(dict)
    exp_dict = copy.deepcopy(dict)
    exp_dict[name] = [amount]
    mail.update_donors(name,amount,test_dict)
    assert test_dict == exp_dict

def test3_update_donors():  # checks output when invalid entry is provided
    name = 'Batman'
    amount = 'ten'
    assert mail.update_donors(name,amount,dict) == None

  
# ----- TEST: CREATE REPORT -----
def test_get_report():  # checks report data
    expected = [ ['Name2',200.02,2,100.01], ['Name1',15.20,2,7.60] ]
    assert mail.get_report(dict) == expected


# ----- TEST: SEND LETTERS -----
def test1_send_letters():  # checks that a file is created per donor entry
    mail.send_letters(dict)
    for root, dir, fldr in os.walk('./letters'):
        assert any(f=='Name1.txt' for f in fldr)
        assert any(f=='Name1.txt' for f in fldr)
        
def test2_send_letters():  # checks output when letters already exist 
    assert mail.send_letters(dict) == None
    
def test_letter_text():  # checks text of letter 
    name = 'Name1'
    total = sum(dict[name])
    expected_text = "\n".join(("Dear Name1,\n", 
        "\tThank you for your generous donations totaling $15.20.\n", 
        "\tIt will be put to very good use.\n",
        "\t\tSincerely,",
        "\t\t  -The Team"))
    assert mail.letter_text(name,total) == expected_text
