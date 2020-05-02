# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: test_mailroom
# Desc: Unit Testing
# ------------------------------------------------------------------------#

import mailroom4
import os
import pytest

dict_of_donors = {'Jeff Bezos': [1.00, 50.00],
                  'Warren Buffet': [100.00, 1000.00],
                  'Bill Gates': [100.00, 500.00],
                  'Tim Cook': [300.00],
                  'Jack Ma': [2000.00]}

def test_show_donor_dict():
    """Test show_donor_dict function """
    result = mailroom4.show_donor_dict(dict_of_donors)
    assert result[0] == 'Jeff Bezos'
    assert result[1] == 'Warren Buffet'
    assert result[2] == 'Bill Gates'
    assert result[3] == 'Tim Cook'
    assert result[4] == 'Jack Ma'


def test_adding_donor_info():
    """Test adding_donor_info function """
    mailroom4.adding_donor_info('Michael Jordan', 23, mailroom4.dict_of_donors)
    assert 'Michael Jordan' in mailroom4.dict_of_donors
    assert mailroom4.dict_of_donors['Michael Jordan'] == [23]

def test_create_email():
    result = mailroom4.create_email('test', 100)
    assert result[0] == "=======Email Template======="
    assert result[1] == 'Dear test,\n\nThank you for your generosity, your donation of $100.00 will be put to good use.\n\n''Warm regards,\nMailroom Staff'

def get_letter_text(name):
    """Get letter text for file content"""
    with open('{}.txt'.format(name), 'r') as file:
        letter = file.readlines()
    return letter

def test_send_all():
    """Test the send_all function"""
    mailroom4.send_all()
    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('Warren_Buffet.txt')
    assert os.path.isfile('Bill_Gates.txt')
    assert os.path.isfile('Tim_Cook.txt')
    assert os.path.isfile('Jack_Ma.txt')
    expected_letter = ['Dear Jeff Bezos,\n', '\n', 'Thank you for your generosity, your donation of $50.00 will be put to very good use.\n', '\n', 'Your total donation amount is $51.00.\n', '\n', 'Warm regards,\n', 'Mailroom Staff']
    assert get_letter_text('Jeff_Bezos') == expected_letter

def test_create_report():
    """Test the create_report function"""
    report = mailroom4.create_report_format()
    assert report[0] == 'Donor Name                | Total Given | Num Gifts | Average Gift'
    assert report[1] == '------------------------------------------------------------------'
    assert report[2] == 'Jack Ma                    $    2000.00           1  $     2000.00'
    assert report[3] == 'Warren Buffet              $    1100.00           2  $      550.00'
    assert report[4] == 'Bill Gates                 $     600.00           2  $      300.00'
    assert report[5] == 'Tim Cook                   $     300.00           1  $      300.00'
    assert report[6] == 'Jeff Bezos                 $      51.00           2  $       25.50'

if __name__== "__main__":
    test_show_donor_dict()
    test_adding_donor_info()
    test_create_email()
    test_send_all()
    test_create_report()
    print("Passed")

