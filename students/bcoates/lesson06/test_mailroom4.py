#!/usr/bin/env python3

import mailroom4 as mailroom
import os

def test_create_a_report():
    report_output = ['Cheryl Tunt          $    98,342.30           2     49,171.15', 
                    'Pam Poovey           $    80,891.30           3     26,963.77', 
                    'Ray Gillette         $     3,820.90           1      3,820.90', 
                    'Lana Kane            $     2,999.99           1      2,999.99', 
                    'Cyril Figgis         $     1,828.37           3        609.46']
    assert mailroom.create_a_report() == report_output

def test_add_donor():
    # Test for existing donor
    assert mailroom.add_donor('Lana Kane') == None
    assert mailroom.donor_history['Lana Kane'] == [2999.99]
    
    # Test for new donor
    mailroom.add_donor('Test User')
    assert mailroom.donor_history['Test User'] == []

def test_add_donation_amount():
    # Test adding a donation to an existing donor
    mailroom.add_donation_amount('Lana Kane', 50.25) == 50.25
    assert mailroom.donor_history['Lana Kane'] == [2999.99, 50.25]

def test_format_thank_you_letter():
    letter_output = "\nDear Test User,\n\nThank you for your generous donation of $75.50!\n\nSincerely,\n\nThe Owners"
    assert mailroom.format_thank_you_letter('Test User', 75.50) == letter_output

def test_save_file():
    test_file = mailroom.save_file("Test User", "Empty Text")
    assert os.path.isfile(test_file) is True