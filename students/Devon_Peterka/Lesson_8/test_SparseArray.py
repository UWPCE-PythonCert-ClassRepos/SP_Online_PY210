#!/usr/bin/env python3

import unittest
from SparseArray import SparseArray

class Test_SA(unittest.TestCase):
    def setUp(self):
        self.sa = SparseArray([1,0,2,0,3,0,4,0,0,6])

    def test_length(self):
        '''
        Verifies the length attribute behaves as expected
        (i.e. - adds zeros)
        '''
        self.assertEqual(len(self.sa), 10)

    def test_save(self):
        '''
        Verify data is saved as expected.
        (i.e. - as a dictionary with only indices and non-zero values)
        '''
        self.assertEqual(self.sa.save, {0:1, 2:2, 4:3, 6:4, 9:6})

    def test_indexing(self):
        '''
        Verify data can be called by index location.
        '''
        self.assertEqual(self.sa[1], 0)
        self.assertEqual(self.sa[4], 3)
        with self.assertRaises(IndexError):
            self.sa[10]
#        self.assertRaises(IndexError, self.sa[10])

    def test_slicing(self):
        '''
        Verify slicing works
        '''
        self.assertEqual(self.sa[1:-1], [0,2,0,3,0,4,0,0])
        self.assertEqual(self.sa[:5:2], [1,2,3])

    def test_setvalue(self):
        '''
        Verify sparse array can be modified.
        '''
        self.sa[1] = 9
        self.assertEqual(list(self.sa), [1,9,2,0,3,0,4,0,0,6])
        
    def test_delete(self):
        '''
        Verify delete call works properly.
        '''
        del self.sa[4]
        self.assertEqual(list(self.sa), [1,0,2,0,0,4,0,0,6])

    def test_append(self):
        '''
        Verify append functionality works properly.
        '''
        self.sa.append([5,4,0,0,2])
        self.assertEqual(len(self.sa), 15)
        self.assertEqual(list(self.sa), [1,0,2,0,3,0,4,0,0,6,5,4,0,0,2])
