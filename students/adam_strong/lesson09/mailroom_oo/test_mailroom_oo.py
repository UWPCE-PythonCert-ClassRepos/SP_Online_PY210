#!/usr/bin/env python3

""" Tests functionality of mailroom_oo package through cli_main.py and donor_models.py
"""
import donor_models as dm
import cli_main as cli

import sys
from mock import patch
from io import StringIO
import pathlib
import os
import pytest


# Data to check against

expected_report = ['\n',
                   'Donor Name          |     Total Given|      Num Gifts|    Average Gift',
                   '------------------------------------------------------------------------',
                   'Richie Rich          $     1500000.00                2  $      750000.00',
                   'Scrooge McDuck       $       78000.00                2  $       39000.00',
                   'Chet Worthington     $       54787.63                3  $       18262.54',
                   'Montgomery Burns     $          49.53                1  $          49.53',
                   'Silas Skinflint      $           1.68                3  $           0.56']

expected_write_letter = '\nDear Montgomery Burns,\n\n    Thank you\
 for your very kind donations totaling $49.53.\n\n    It will be put\
 to very good use.\n\n               Sincerely,\n                  - The team'
monty_name = "Montgomery Burns"
monty_value = [49.53]
thanks_newberry = '\nDear John Newberry\nThank you for your generous donation of 5.00\n'
thanks_silas = '\nDear Silas Skinflint\nThank you for your generous donation of 500.00\n'
filelist = ['Montgomery_Burns.txt', 'Richie_Rich.txt', 'Chet_Worthington.txt',
            'Silas_Skinflint.txt', 'Scrooge_McDuck.txt']
newberry_addition = {"John Newberry": [5.00]}
invalid_selection = '----> Invalid Selection: Please input a number 1-4'
invalid_amount = '--->Not a valid amount, please try your submission again'
richie_line = 'Richie Rich          $         600.00                2  $         300.00'


# TESTS:

def test_exit():
    '''Tests that the code exits on a selection of 4'''
    with patch('sys.exit') as exit_mock:
        cli.exit_program()
        assert exit_mock.called is True


def test_list_invoked_notlist():
    '''Tests that a value other than 'list' gets passed through'''
    assert cli.list_invoked('cat') == 'cat'


def test_list_invoked_list():
    '''Tests that a value of 'list' executes the report function'''
    with patch('cli_main.report') as report_mock:
        cli.list_invoked('list')
        assert report_mock.called is True


def test_invalid_amt():
    '''Tests that an invalid amount creates an error'''
    with patch('sys.stdout', new=StringIO()) as fake_output:
        cli.amt_logic('name', 'blah')
        assert fake_output.getvalue().strip() == invalid_amount


def test_invalid_neg_amt():
    '''Tests that a negative amount creates an error'''
    with patch('sys.stdout', new=StringIO()) as fake_output:
        cli.amt_logic('name', -20)
        assert fake_output.getvalue().strip() == invalid_amount


def test_switch_bad1():
    '''Tests that an invalid main reponse creats an error - for type:str'''
    with patch('sys.stdout', new=StringIO()) as fake_output2:
        cli.main_switch('dog')
        assert fake_output2.getvalue().strip() == invalid_selection


def test_switch_bad2():
    '''Tests that an invalid main reponse creats an error - for invalid integer'''
    with patch('sys.stdout', new=StringIO()) as fake_output3:
        cli.main_switch(5)
        assert fake_output3.getvalue().strip() == invalid_selection


def test_report():
    '''Tests the report function in DonorCollections class'''
    data = cli.data
    report = data.make_report()
    assert report == expected_report


def test_write_letter():
    '''Tests the write_letter function in Donor class'''
    don = dm.Donor(monty_name, monty_value)
    form_letter = don.write_letter()
    assert form_letter == expected_write_letter


def test_thankyou_main():
    '''Tests the main thank_you function in cli_main'''
    with patch('cli_main.input', return_value='4') as tyinput_mock, \
    patch('cli_main.list_invoked') as listmock, \
    patch('cli_main.amt_logic') as amtlogicmock:
        cli.thank_you()
        assert tyinput_mock.called is True
        assert listmock.called is True
        assert amtlogicmock.called is True
        assert tyinput_mock.call_count == 2


def test_add_donor():
    '''Tests the add_donor function with novel name in DonorCollections class'''
    data = cli.data
    ty_output = data.add_donor('John Newberry', 5.00)
    assert ty_output == thanks_newberry
    assert data.donors['John Newberry'].value == [5.00]
    del data.donors['John Newberry']


def test_add_donation_existing():
    '''Tests the add_donor function with existing name in DonorCollections class'''
    data = cli.data
    ty_output = data.add_donor('Silas Skinflint', 500.00)
    assert ty_output == thanks_silas
    assert data.donors['Silas Skinflint'].value == [0.25, 1.00, 0.43, 500.00]
    data.donors['Silas Skinflint'].value.pop(3)


def test_add_donation_existing_lower_case_input():
    '''Tests the add_donor function with existing name in DonorCollections class
    when the user does not capitalize either of the names'''
    data = cli.data
    ty_output = data.add_donor('silas skinflint', 500.00)
    assert ty_output == thanks_silas
    assert data.donors['Silas Skinflint'].value == [0.25, 1.00, 0.43, 500.00]
    data.donors['Silas Skinflint'].value.pop(3)


def test_report2():
    '''Validates that report still functions from previous tests'''
    data = cli.data
    report = data.make_report()
    assert report == expected_report


def test_file_creation():
    '''Tests the create_letter function in the Donor class'''
    don = dm.Donor('File Flisby', [400.00, 800.00, 1200.00])
    don.create_letter()
    testpth = pathlib.Path('./')
    testdest = testpth.absolute() / 'File_Flisby.txt'
    assert os.path.isfile(testdest) is True


def test_send_letter():
    '''Tests the send_letter function in the DonorCollections class'''
    data = cli.data
    data.send_letter()
    testpth = pathlib.Path('./')
    for filesel in filelist:
        testdest = testpth.absolute() / filesel
        assert os.path.isfile(testdest) is True


def test_format_donor():
    '''Tests the format_donor function in the Donor class'''
    don = dm.Donor('Richie Rich', [400.00, 200.00])
    richie = don.format_donor()
    assert richie == richie_line
