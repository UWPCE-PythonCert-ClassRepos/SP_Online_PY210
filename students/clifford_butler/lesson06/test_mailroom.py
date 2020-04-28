#!/usr/bin/env python3

'''
Mailroom Part 4
Add a full suite of unit tests.
'''

import mailroom4 as mr
import names
import sys 
from mock import patch

def test_get_index():
    '''
    test get index function
    '''
    pass
    

def test_add_donor():
    '''
    test add donor function
    '''
    assert 'William Gates, III' in donor_dict
    assert 'Jeff Bezos' in donor_dict
    assert 'Paul Allen' in donor_dict
    assert 'Mark Zuckerberg' in donor_dict
    assert 'Alexandra Butler' in donor_dict
    assert names.get_full_name() not in donor_dict
    
def test_view_list():
    '''
    test view list function
    '''
    pass

def test_display_dict():
    '''
    test display dictionary function
    '''
    pass

def test_send_thank_you():
    '''
    test send thank you function
    '''
    pass

def test_create_report():
    '''
    test create report function
    '''
    pass

def test_letter_to_all():
    '''
    test letter to all function
    '''
    pass

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
    test_view_list()
    print('test_view_list passed')
    test_display_dict()
    print('test_display_dict passed')        
    test_send_thank_you()
    print('test_send_thank_you passed') 
    test_create_report()    
    print('test_create_report passed')    
    test_letter_to_all()
    print('test_letter_to_all passed')        
    test_exit_program()
    print('test_exit_program passed')


  

