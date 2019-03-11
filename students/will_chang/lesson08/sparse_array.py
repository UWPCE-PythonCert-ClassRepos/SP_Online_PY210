#!/usr/bin/env python

class SparseArray:
    def __init__(self, arr):
        self.len = len(arr)
        self.sparse = {index: item for index, item in enumerate(arr) if item}

    def __getitem__(self, index):
        if isinstance(index, slice):
            start = 0 if index.start is None or index.start < 0 else index.start
            stop = self.len if index.stop is None or index.stop > self.len else index.stop
            step = 1 if index.step is None else index.step

            return [self.sparse.get(i, 0) for i in range(start, stop, step)]
        elif index >= 0 and index < self.len:
            return self.sparse.get(index, 0)
        elif index < 0:
            return self.sparse.get(self.len + index, 0)
        else:
            raise IndexError
        
    def __setitem__(self, index, value):
        if value != 0:
            self.sparse[index] = value
        else:
            try:
                del self.sparse[index]
            except KeyError:
                pass
    
    def __delitem__(self, index):
        del self.sparse[index]
    
    def __len__(self):
        return self.len
    
    def append(self, value):
        if value != 0:
            self.sparse[self.len] = value
            self.len += 1
    
if __name__ == "__main__":
    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])