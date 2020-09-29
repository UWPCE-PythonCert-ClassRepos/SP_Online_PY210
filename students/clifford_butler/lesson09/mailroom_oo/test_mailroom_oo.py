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
    d3 = Donor('Mark Zuckerberg')
    z = [1663.23, 4300.87, 10432.0]
    for amount in z:
        d3.add_amount(amount)        
    assert d3.donations == z  
    assert d3.total_donations() == 16396.1 
    assert d3.last_donation() == 10432.0
    assert d3.average_donation() == 5465.366666666666
    assert d3.num_donations() == 3

    print('add donation test passed')
    
def test_empty():
    '''
    test returning empty/zero values
    '''
    a = Donor('Clifford Butler')
    assert a.last_donation() == 0
    assert a.total_donations() == 0
    assert a.average_donation() == 0
    assert a.num_donations() == 0
    print ('test empty passed')

def test_exit_program():
    '''
    test exit function 
    '''
    with patch('sys.exit') as exit_mock:
        cm.exit_program()
        assert exit_mock.called == True
        assert exit_mock.called != False
        
    print ('test exit passed')     

if __name__== "__main__":
    test_donor_init()
    test_add()
    test_empty()
    test_exit_program()
    print('All test passed')
    
