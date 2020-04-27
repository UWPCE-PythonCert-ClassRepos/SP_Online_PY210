#!/usr/bin/env python3

'''
Mailroom Part 4
Add a full suite of unit tests.
'''

import mailroom4 as mr
import names

def test_get_index():
    '''
    test if the hard coded names return the correct index number
    test if a names not in the dictionary return None
    '''
    assert mr.get_index('William Gates, III') == 0 
    assert mr.get_index('Jeff Bezos') == 1
    assert mr.get_index('Paul Allen') == 2
    assert mr.get_index('Mark Zuckerberg') == 3
    assert mr.get_index('Alexandra Butler') == 4
    assert mr.get_index(names.get_full_name()) == None

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

if __name__== "__main__":
    test_add_donor()
    print('test_get_index passed')

