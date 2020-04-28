#!/usr/bin/env python3

'''
Mailroom Part 4
Add a full suite of unit tests.
'''

import mailroom4 as mr
import names
import sys 
from mock import patch

dupl_dict = mr.donor_dict

def test_get_index():
    '''
    test if the hard coded names return the correct index number
    test if a names not in the dictionary return None
    '''
    print(' ')
    

def test_add_donor():
    '''
    test if the hard coded names are in donor_dict
    test if the function validates names that aren't 
    in the dictionary
    '''
    assert 'William Gates, III' in mr.donor_dict
    assert 'Jeff Bezos' in mr.donor_dict
    assert 'Paul Allen' in mr.donor_dict
    assert 'Mark Zuckerberg' in mr.donor_dict
    assert 'Alexandra Butler' in mr.donor_dict
    assert names.get_full_name() not in mr.donor_dict

def test_exit_program():
    '''
    test exit function 
    '''
    with patch('sys.exit') as exit_mock:
        exit_program()
        assert exit_mock.called == True

if __name__== "__main__":
    test_get_index()
    print('test_get_index passed')
    test_add_donor()
    print('test_add_donor passed')
    '''
    test_view_list()
    print('passed')
    test_display_dict()
    print('passed')        
    test_send_thank_you()
    print('passed') 
    test_create_report()    
    print('passed')    
    test_letter_to_all()
    print('passed')        
    '''
    test_exit_program()
    print('test_exit_program passed')


  

