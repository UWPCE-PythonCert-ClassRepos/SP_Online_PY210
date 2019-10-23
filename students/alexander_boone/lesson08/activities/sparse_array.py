#!/usr/bin/env python

class SparseArray:

    def __init__(self, sequence):
        self.items = list(sequence)
        self.sparse_array = [item for item in self.items if item != 0]
    
    def __repr__(self):
        return "[" + ", ".join([str(element) for element in self.sparse_array]) + "]"

    def __str__(self):
        return "[" + ", ".join([str(element) for element in self.sparse_array]) + "]"

    def __len__(self):
        return len(self.sparse_array)

    def __reversed__(self):
        return self.sparse_array[::-1]
    
    def __getitem__(self, key):
        try:
            return self.sparse_array[key]
        except IndexError:
            return 0

    def __setitem__(self, key, value):
        if key != 0:
            self.sparse_array[key] = value
    
    def __delitem__(self, key):
        self.sparse_array.pop(key)

    def __iter__(self):
        pass
    
    def __contains__(self, item):
        if item in self.sparse_array:
            return True
        else:
            return False
    
    def append(self, item):
        if item != 0:
            self.sparse_array.append(item)