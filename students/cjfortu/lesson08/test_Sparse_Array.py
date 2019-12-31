#!/usr/bin/env python

import pytest
from Sparse_Array import *


def test_non_zero_indexes():
    sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
    assert 0 not in list(sa)
    
def test_length():
    sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
    assert sa.length == 12
    
def test_getting():
    sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
    assert sa[0] == 0
    assert sa[11] == 21
    
def test_setting():
    sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
    sa[4] = 0
    assert sa.values == {1: 1, 2: 1, 5: 3, 7: 5, 8: 8, 10: 13, 11: 21}
    assert sa.length == 12
    sa[4]= 20
    assert sa.values == {1: 1, 2: 1, 4: 20, 5: 3, 7: 5, 8: 8, 10: 13, 11: 21}
    assert sa.length == 12
    
def test_deleting():
    sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
    del sa[5]
    assert sa.values == {1: 1, 2: 1, 4: 2, 7: 5, 8: 8, 10: 13, 11: 21}
    assert sa.length == 11
    
def test_index_error():
    with pytest.raises(IndexError, match='cannot access index beyond end'):
        sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
        sa[13]
    with pytest.raises(IndexError, match='cannot access index beyond end'):
        sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
        sa[13] = 0
    with pytest.raises(IndexError, match='cannot access index beyond end'):
        sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
        sa[13] = 34
        
def test_appending():
    sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
    sa.append(34)
    assert sa.values == {1: 1, 2: 1, 4: 2, 5: 3, 7: 5, 8: 8, 10: 13, 11: 21, 12: 34}
    assert sa.length == 13
    sa.append(55)
    assert sa.length == 14
    
def test_1D_slice():
    sa = Sparse_Array([0, 1, 1, 0, 2, 3, 0, 5, 8, 0, 13, 21])
    assert sa[1:7] == [1, 1, 0, 2, 3, 0]