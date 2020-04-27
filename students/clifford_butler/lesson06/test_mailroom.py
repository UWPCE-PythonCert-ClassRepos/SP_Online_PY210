#!/usr/bin/env python3

'''
Mailroom Part 4
Add a full suite of unit tests.
'''

import mailroom4 as mr

def test_add_donor():
    a = 'William Gates, III'
    b = 'Jeff Bezos'
    c = 'Paul Allen'
    d = 'Mark Zuckerberg'
    e = 'Alexandra Butler'
    assert a in mr.donor_dict
    assert b in mr.donor_dict
    assert c in mr.donor_dict
    assert d in mr.donor_dict
    assert e in mr.donor_dict

if __name__== "__main__":
    test_add_donor()
    print('test_get_index passed')