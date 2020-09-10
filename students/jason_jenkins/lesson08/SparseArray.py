#!/usr/bin/env python3

"""
A class-based system for a SparseArray
"""

class SparseArray(list):

    def __init__(self, l = None):
        if l == None:
            self.l = list()
        else:
            self.l = list(l)

    def __len__(self):
        count = 0
        for item in self.l:
            if item != 0:
                count += 1
        return count


    def __getitem__(self, index):
        return self.l[index]


    def __setitem__(self, key, newvalue):
        if(newvalue != 0):
            self.l[key] = newvalue


    def append(self, val):
        self.l.append(val)


    def __delitem__(self, i):
        del self.l[i]
