class SparseArray():
    def __init__(self, items):
        self.content = {}
        self.length = len(items)
        for key, value in enumerate(items):
            if value:
                self.content[key] = value
  
    def __len__(self):
        return self.length
   
    def __getitem__(self, key):
        #if slice store each item from the slice as a list and return
        if isinstance(key, slice):
            result = []
            indices = key.indices(len(self))
            for k in range(*indices):
                result.append(self[k])
            return result
        #otherwise return the value
        else:
            if key >= self.length:
                raise IndexError
            return self.content.get(key, 0)
    
    def __setitem__(self, key, value):
        #if slice, use __setitem__ to store each value
        if isinstance(key, slice):
            indices = key.indices(len(self))
            for i, k in enumerate(range(*indices)):
                self[k] = value[i]
        #otherwise store the value        
        else:
            #if the value is non zero, store value
            if value: 
                self.content[key] = value
            #if the value is zero, remove item from dict if it is there
            else:
                self.content.pop(key, 0)
            if key >= self.length:
                self.length = key + 1
   
    def __delitem__(self, key):
        if isinstance(key, slice):
            indices = key.indices(len(self))
            for k in reversed(range(*indices)):
                del self[k]
        else:
            #removes item from dict if it is there
            self.content.pop(key, 0)
            self.length -= 1
            #adjust indices for values to the right of deleted value
            keys = [i for i in self.content.keys() if i > key]
            for i in keys:
                self.content[i-1] = self.content.pop(i)
            