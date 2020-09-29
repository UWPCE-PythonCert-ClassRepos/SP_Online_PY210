#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:40:25 2019

@author: humberto
"""

import io
import pytest

from mailroom import *




def test_append_donation_info():
    expected = {"Tyrod Taylor": [1000.00, 45.50],
                "Jarvis Landry": [150.25],
                "Philip Rivers": [650.23, 40.87, 111.32],
                "Melvin Gordon": [1677.25, 4300.23, 10532.00],
                "Mike Williams": [230.56, 12.45, 11.00],
                "Antonio Brown": [100.00, 88.88],
                "Tom Brady": [50.0]
                }
    append_donation_info('Tom Brady',50.0)
    assert donor_db == expected
    print('Test Passed')
    

def test_create_thank_you_txt():
    expected = 'Dear Tom Brady,\n    Thank you for your generous donation of $50.0'
    assert create_thank_you_txt('Tom Brady',50.0) == expected
    print('Test Passed')


def test_create_report():
    expected = [['Melvin Gordon', 16509.48, 3, 5503.16],
                ['Tyrod Taylor', 1045.5, 2, 522.75],
                ['Philip Rivers', 802.42, 3, 267.47],
                ['Mike Williams', 254.01, 3, 84.67],
                ['Antonio Brown', 188.88, 2, 94.44],
                ['Jarvis Landry', 150.25, 1, 150.25],
                ['Tom Brady', 50.0, 1, 50.0]]
    assert create_report(donor_db) == expected
    print('Test Passed')


def test_create_letter_txt():
    expected = '''Dear Tom Brady,\n    Thank you for your generous donation of $50.0. \n    Your donation will be put to great use. \n         Sincerely, \n          -The Organization'''
    assert create_letter_txt('Tom Brady',50.0) == expected
    print('Test Passed.')


def test_send_letters():
    send_letters()   
    for donor in donor_db:
        path = tempfile.gettempdir()
        path = path + "/" + "Letters to Donors"
        temp = path + "/" + donor.replace(' ','_') + '.txt'
        assert os.path.exists(temp)
    print('Test Passed.')
    
    


