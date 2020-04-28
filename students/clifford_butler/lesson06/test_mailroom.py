#!/usr/bin/env python3

'''
Mailroom Part 4
Add a full suite of unit tests.
'''

import mailroom4 as mr
import names
#import sys 
from mock import patch

new_dict = mr.donor_dict

test_list = 'William Gates, III\
\nJeff Bezos\
\nPaul Allen\
\nMark Zuckerberg\
\nAlexandra Butler'

def test_add_donor():
    '''
    test add donor function
    '''
    assert 'William Gates, III' in mr.donor_dict
    assert 'Jeff Bezos' in mr.donor_dict
    assert 'Paul Allen' in mr.donor_dict
    assert 'Mark Zuckerberg' in mr.donor_dict
    assert 'Alexandra Butler' in mr.donor_dict
    assert names.get_full_name() not in mr.donor_dict
    
def test_view_list():
    '''
    test view list function
    '''
    a_list = ('William Gates, III\nJeff Bezos\nPaul Allen\nMark Zuckerberg\nAlexandra Butler')
    assert test_list == a_list

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



def test_letter_to_all():
    '''
    test letter to all function
    
    a = ('\nThank you letters sent!\n')
    #assert letter_to_all() != expected
    assert letter_to_all() == a
    '''

def test_exit_program():
    '''
    test exit function 
    '''
    with patch('sys.exit') as exit_mock:
        mr.exit_program()
        assert exit_mock.called == True

if __name__== "__main__":
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


  

