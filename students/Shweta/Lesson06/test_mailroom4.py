#!/usrbin/env python
#test_mailroom part 4

import mailroom4 as mm
import sys
import pytest
import os
#from unittest.mock import Mock
from mock import patch
from io import StringIO

invalid_amt='Not a valid amount, try again'
mty_msg="\n".join(("Thankyou {}",
                   "for your generous donation of {:.2f}",))
list_orig="""
Donor Name          |          Total Given|           Num Gifts|         Average Gift
----------------------------------------------------------------------------------------------------
William Gate,III     $           145000.00                      2   $            72500.00
Mark Zuckerbergs     $            18300.00                      2   $             9150.00
Jeff Bezos           $            25257.00                      3   $             8419.00
Paul Allen           $             3545.00                      2   $             1772.50
"""

def test_response():
    error_response="Please do select between 1-4,try again"
    with patch('sys.stdout',new=StringIO()) as error_resp:
        mm.main_decision(5)
        assert error_resp.getvalue().strip() == error_response
        
    
def test_list():
    with patch('mailroom4.create_report') as list_v:
        mm.print_list('list')
        assert list_v.called is True
        
def test_donation_amt():
    dname='test'
    assert mm.amt_validation(dname,0)== 0.0
    assert mm.amt_validation(dname,45)== 45.0
    assert mm.amt_validation(dname,3524)== 3524.0

    
def test_amt_validation():
    name='shweta'
    with patch('mailroom4.amt_validation') as valid_amt:
        mm.amt_validation('name',45)
        assert valid_amt.called is True

def test_invalid_amt():
    name='singh'
    with patch('sys.stdout', new=StringIO()) as invalid_damt:
        mm.amt_validation('name','abc')
        assert invalid_damt.getvalue().strip() == invalid_amt

def test_thanks_msg():
    
    name='Bill Braham'
    damt=1211.11
    assert mm.add_thanks(name,damt) == mty_msg.format(name,damt)

def test_name_exist():
    name="Jeff Bezos"
    damt=54378.90
    assert mm.add_thanks(name,damt) == mty_msg.format(name,damt)
    with patch('mailroom4.create_report') as list_op:
        mm.print_list('list')
        assert list_op.called is True
        
#def test_thanks_ltr():
#    assert mm.add_thanks('Shweta',1211.11)==test_thanks_msg('Shweta',1211.11)

    
