#!/usr/bin/env python3

from SparseArray import SparseArray

def test_length():
    '''
    Verifies the length attribute behaves as expected
    (i.e. - adds zeros)
    '''
    sa = SparseArray([1,0,2,0,3,0,4,0])
    assert(len(sa)==8)

def test_save():
    '''
    Verify data is saved as expected.
    (i.e. - as a dictionary with only indices and non-zero values)
    '''
    sa = SparseArray([1,0,2,0,3,0,4,0])
    assert(sa.save == {0:1, 2:2, 4:3, 6:4})

def test_indexing():
    '''
    Verify data can be called by index location.
    '''
    sa = SparseArray([1,0,2,0,3,0,4,0])
    assert(sa[1]==0)
    assert(sa[4]==3)

def test_setvalue():
    '''
    Verify sparse array can be modified.
    '''
    sa = SparseArray([1,0,2,0,3,0,4,0])
    sa[1] = 9
    assert(sa==[1,9,2,0,3,0,4,0])
    
    
