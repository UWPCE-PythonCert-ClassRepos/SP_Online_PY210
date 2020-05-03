#!/usr/bin/env python3

"""
Test functions for mailroom_oo
"""

from donor_models import Donor, DonorCollection
import cli_main as cm
from mock import patch
import pytest

def test_donor_init():
    '''
    test donor init function
    '''
    d = Donor('Clifford Butler')

    with pytest.raises(TypeError):
        d = Donor()
        assert pytest.raises == True
        assert pytest.raises != False
        
    print('donor init test passed')
    
def test_add():
    '''
    test add donation function
    '''
    d = Donor('Clifford Butler')
    z = [100.00, 50.00, 150.00]
    for amount in z:
        d.add_amount(amount)
    assert d.donations == z  
    print(d.donations)
    assert d.last_donation() == 150.00
    #assert d.total_donations() == 300.00
    #assert d.average_donation() == 100.00
    #assert d.num_donations() == 3
    
    print('add donation test passed')

def test_thank_you_text():
    '''
    test thank you text function
    '''
    pass

def test_add_name():
    '''
    test add name function
    '''
    pass

def test_prompt_amount():
    '''
    test prompt amount function
    '''
    pass
    
def test_add_amount():
    '''
    test add amount function
    '''
    pass 

def test_exit_program():
    '''
    test exit function 
    '''
    with patch('sys.exit') as exit_mock:
        cm.exit_program()
        assert exit_mock.called == True
        assert exit_mock.called != False

if __name__== "__main__":
    test_donor_init()
    test_add()
    #test_thank_you_text()
    #test_add_name()
    #test_prompt_amount()
    #test_add_amount()
    #test_exit_program()
    print('All test passed')
    
