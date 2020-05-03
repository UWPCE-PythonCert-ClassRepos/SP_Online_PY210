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
    d = Donor('Reem Alqaysi')

    with pytest.raises(TypeError):
        d = Donor()
        assert pytest.raises == True
        
    print('donor init test passed')

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
    test_thank_you_text()
    test_add_name()
    test_prompt_amount()
    test_add_amount()
    test_exit_program()
    print('All test passed')
    
