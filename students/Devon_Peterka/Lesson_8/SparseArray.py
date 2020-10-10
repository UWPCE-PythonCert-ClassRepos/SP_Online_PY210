#!/usr/bin/env python3

class SparseArray:
    def __init__(self, input):
        '''
        Saves the length of the original object and truncates zeroes and stores
        remaining values into memory.
        '''
        self._len = len(input)
        self.save = {i: input[i] for i in range(self._len) if input[i] != 0}
 
    def __len__(self): return self._len

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.save[index] if index in self.save.keys() else 0
#        elif isinstance(index, slice):
            

    def __setitem__(self, index):
        if index <= self._len-1:
            
