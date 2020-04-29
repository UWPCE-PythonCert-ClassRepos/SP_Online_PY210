#!/usr/bin/env python3
# test_mailroom4.py - Lesson06 - Assignment 5 - Unittesting with Pytest
from mailroom4 import *
import sys
from mock import patch
from io import StringIO
import pathlib
import os
import pytest

# Data to check against

expected_report = 'Donor Name          |     Total Given|      Num Gifts|    Average Gift\
\n------------------------------------------------------------------------\
\nRichie Rich          $     1500000.00                2  $      750000.00\
\nScrooge McDuck       $       78000.00                2  $       39000.00\
\nChet Worthington     $       54787.63                3  $       18262.54\
\nMontgomery Burns     $          49.53                1  $          49.53\
\nSilas Skinflint      $           1.68                3  $           0.56'

expected_write_letter = '\nDear Montgomery Burns,\n\n    Thank you\
 for your very kind donations totaling $49.53.\n\n    It will be put\
 to very good use.\n\n               Sincerely,\n                  - The team'
monty_name = "Montgomery Burns"
monty_value = [49.53]
thanks_newberry = 'Dear John Newberry\nThank you for your generous donation of 5.00'
thanks_silas = 'Dear Silas Skinflint\nThank you for your generous donation of 500.00'
newberry_db = {"Scrooge McDuck": [8000.00, 70000.00],
               "Montgomery Burns": [49.53],
               "Richie Rich": [1000000.00, 500000.00],
               "Chet Worthington": [200.00, 44387.63, 10200.00],
               "Silas Skinflint": [0.25, 1.00, 0.43],
               "John Newberry": [5.00]}
filelist = ['Montgomery_Burns.txt', 'Richie_Rich.txt', 'Chet_Worthington.txt',
            'Silas_Skinflint.txt', 'Scrooge_McDuck.txt']
newberry_addition = {"John Newberry": [5.00]}
invalid_selection = '----> Invalid Selection: Please input a number 1-4'
invalid_amount = '--->Not a valid amount, please try your submission again'

# TEST exit_program():

def test_exit():
    with patch('sys.exit') as exit_mock:
        exit_program()
        assert exit_mock.called is True


# TEST list_invoked():

def test_list_invoked_notlist():
    assert list_invoked('cat') == 'cat'


def test_list_invoked_list():
    with patch('mailroom4.report') as report_mock:
        list_invoked('list')
        assert report_mock.called is True


# TEST amt_logic():

def test_valid_amt():
    with patch('mailroom4.ty_logic') as tylogic_mock:
        amt_logic('name', 43)
        assert tylogic_mock.called is True


def test_invalid_amt():
    with patch('sys.stdout', new=StringIO()) as fake_output:
        amt_logic('name', 'blah')
        assert fake_output.getvalue().strip() == invalid_amount


# TEST main_switch()

def test_switch_bad1():
    with patch('sys.stdout', new=StringIO()) as fake_output2:
        main_switch('dog')
        assert fake_output2.getvalue().strip() == invalid_selection


def test_switch_bad2():
    with patch('sys.stdout', new=StringIO()) as fake_output3:
        main_switch(5)
        assert fake_output3.getvalue().strip() == invalid_selection


# TEST report()
def test_report():
    with patch('sys.stdout', new=StringIO()) as fake_output4:
        report()
        assert fake_output4.getvalue().strip() == expected_report


# TEST write_letter():
def test_write_letter():
    form_letter = write_letter(monty_name, monty_value)
    assert form_letter == expected_write_letter


# TEST ty_logic():
def test_thankyou_main():
    with patch('mailroom4.input', return_value='4') as tyinput_mock, \
    patch('mailroom4.list_invoked') as listmock, \
    patch('mailroom4.amt_logic') as amtlogicmock:
        thank_you()
        assert tyinput_mock.called is True
        assert listmock.called is True
        assert amtlogicmock.called is True
        assert tyinput_mock.call_count == 2


def test_ty_logic_new():
    with patch('sys.stdout', new=StringIO()) as ty_output:
        ty_logic('John Newberry', 5.00)
        assert ty_output.getvalue().strip() == thanks_newberry
        assert donor_db['John Newberry'] == [5.0]
        del donor_db['John Newberry']

# TEST report()
def test_report2():
    '''In order to check that test_ty_logic_new() was reset'''
    with patch('sys.stdout', new=StringIO()) as fake_output4:
        report()
        assert fake_output4.getvalue().strip() == expected_report


def test_ty_logic_update():
    with patch('sys.stdout', new=StringIO()) as ty_output2:
        ty_logic('Silas Skinflint', 500.00)
        assert ty_output2.getvalue().strip() == thanks_silas
        assert donor_db['Silas Skinflint'] == [0.25, 1.00, 0.43, 500.00]
        donor_db['Silas Skinflint'].pop(3)

def test_report3():
    '''In order to check that test_ty_logic_update() was reset'''
    with patch('sys.stdout', new=StringIO()) as fake_output4:
        report()
        assert fake_output4.getvalue().strip() == expected_report

# TEST create_text_file():
def test_file_creation():
    create_text_file('File Flisby', [400.00, 800.00, 1200.00])
    testpth = pathlib.Path('./')
    testdest = testpth.absolute() / 'File_Flisby.txt'
    assert os.path.isfile(testdest) is True


def test_send_letter():
    send_letter()
    testpth = pathlib.Path('./')
    for filesel in filelist:
        testdest = testpth.absolute() / filesel
        assert os.path.isfile(testdest) is True
