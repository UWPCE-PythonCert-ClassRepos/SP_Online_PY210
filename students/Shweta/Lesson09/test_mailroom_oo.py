#!/usrbin/env python
#test_mailroom object oriented code

import donor_model as mm
import cli_main as cm
import sys
import pathlib
import pytest
import os
#from unittest.mock import Mock
from mock import patch
from io import StringIO

invalid_amt='Negative Value not allowed'
mty_msg="\n".join(("Thankyou {}",
                   "for your generous donation of {:.2f}",))

expected_output=['William Gate,III     $           145000.00                    2   $            72500.00',
                 'Mark Zuckerbergs     $            18300.00                    2   $             9150.00', 
                 'Jeff Bezos           $            24600.00                    2   $            12300.00', 
                 'Paul Allen           $             3545.00                    2   $             1772.50', 
                 'test                 $               45.00                    2   $               22.50']

list_orig="""
Donor Name          |          Total Given|           Num Gifts|         Average Gift
----------------------------------------------------------------------------------------------------
William Gate,III     $           145000.00                      2   $            72500.00
Mark Zuckerbergs     $            18300.00                      2   $             9150.00
Jeff Bezos           $            25257.00                      3   $             8419.00
Paul Allen           $             3545.00                      2   $             1772.50
"""

file_list=["William_Gate,III.txt","Paul_Allen.txt","Mark_Zuckerbergs.txt","Jeff_Bezos.txt"]

def test_response():
    error_response="Please do select between 1-4,try again"
    with patch('sys.stdout',new=StringIO()) as error_resp:
        cm.main_decision(5)
        assert error_resp.getvalue().strip() == error_response
        
def test_name_taken():
    assert cm.print_list("ssingh") == "ssingh"

def test_list():
    with patch('cli_main.create_report') as list_v:
        cm.print_list('list')
        assert list_v.called is True
        
def test_donation_amt():
    dname='test'
    assert cm.amt_validation(dname,0)== 0.0
    assert cm.amt_validation(dname,45)== 45.0


def test_amt_validation():
    name='shweta'
    with patch('cli_main.amt_validation') as valid_amt:
        cm.amt_validation('name',45)
        assert valid_amt.called is True

def test_invalid_amt():
    name='singh'
    with patch('sys.stdout', new=StringIO()) as invalid_damt:
        cm.amt_validation('name',-3)
        assert invalid_damt.getvalue().strip() == invalid_amt

def test_invalid_amt_type():
    name='singh'
    with patch('sys.stdout', new=StringIO()) as invalid_damt:
        cm.amt_validation('name','shweta')
        assert invalid_damt.getvalue().strip() == "Not a valid amount, try again"


def test_name_exist():
    name="Jeff Bezos"
    damt=54378.90
    with patch('cli_main.create_report') as list_op:
        cm.print_list('list')
        assert list_op.called is True

def test_quit_pgm():
    with pytest.raises(SystemExit) as qp:
        cm.quit_pgm()
        assert qp.type == SystemExit
        assert qp.value.code == 42

def test_main_decision_str():
    with patch('sys.stdout', new=StringIO()) as wrong_decision:
        cm.main_decision('ssingh')
        assert wrong_decision.getvalue().strip() == "Please do select between 1-4,try again"
       
def test_main_decision_int():
    with patch('sys.stdout', new=StringIO()) as wrong_decision:
        cm.main_decision(6)
        assert wrong_decision.getvalue().strip() == "Please do select between 1-4,try again"



def test_create_report():
    db=cm.donor_db
    final_report=cm.create_report()
    assert final_report == expected_output

def test_name_printed():
    assert cm.print_list('Shweta') == 'Shweta'


def test_file_creation():
    dn=mm.Donor('Singh',[120.00,876.00])
    dn.ind_thankyou()
    testpath=pathlib.Path('./')
    testdpath=testpath.absolute() / 'Singh.txt'
    assert os.path.isfile(testdpath) is True

def test_send_letter():
    dn=cm.donor_db
    dn.send_letter()
    testpath=pathlib.Path('./')
    for files in file_list:
        testdpath=testpath.absolute() / files
        assert os.path.isfile(testdpath) is True
