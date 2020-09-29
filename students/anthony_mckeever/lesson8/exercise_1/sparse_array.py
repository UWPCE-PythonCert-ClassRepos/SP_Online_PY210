"""
Programming In Python - Lesson 8 Exercise 1: Sparse Array
Code Poet: Anthony McKeever
Start Date: 09/04/2019
End Date: 09/04/2019
"""

class SparseArray():
    """
    An array object that doesn't store zeros but will still return them if an index with zero is retrieved.
    """

    def __init__(self, input):
        """
        Initialize the SparseArray

        :self:  The Class
        :input: The list to turn into a SparseArray.
        """
        self._len = len(input)
        self.storage = {k: input[k] for k in range(self._len) if input[k] != 0 }


    def __len__(self):
        """
        Return the length of the sparse array including zeros.
        """
        return self._len
    

    def __getitem__(self, index):
        """
        Return the item(s) at the index or within the slice

        :self:  The Class
        :index: The index or slice
        """
        if isinstance(index, int):
            index = self.validate_index(index)

            item = self.storage.get(index)
            return item if item is not None else 0
        
        elif isinstance(index, slice):
            get_range = self.get_range(index)
            print(get_range)
            return [self.__getitem__(x) for x in get_range]
        
        else:
            raise TypeError(f"SparseArray indicies must be integers or slices, not {type(index).__name__}")

    
    def __setitem__(self, index, value):
        """
        Set the item at the index

        :self:  The Class
        :index: The index of the item to change.
        :value: The new value for the item at the index.
        """
        index = self.validate_index(index)
          
        if index in self.storage.keys():
            if value != 0:
                self.storage[index] = value
            else:
                self.storage.pop(index)
        else:
            # No need to check if the index is in range as the call to self.validate_index above has already done that.
            if value != 0:
                self.storage.update({index: value})


    def append(self, value):
        """
        Append an item to the SparseArray

        :self:  The classs
        :value: The item to append
        """
        if value != 0:
            item = {self._len: value}
            self.storage.update(item)
        self._len += 1


    def validate_index(self, index):
        """
        Validate that the desired index is in range.

        :self:  The Class
        :index: The index to validate
        """
        index = index if index >= 0 else self._len + index 
        
        if index >= self._len or index < 0:
            raise IndexError("SparseArray index out of range.")

        return index


    def get_range(self, slice_index):
        """
        Return a range from a slice.
        
        :self:          The Class
        :slice_index:   The slice to convert into a range.
        """
        step =  slice_index.step if slice_index.step is not None else 1
        start = slice_index.start
        stop =  slice_index.stop

        if start is None:
            start = self._len - 1 if step < 0 else 0

        if stop is None:
            stop = -1 if step < 0 else self._len

        return range(start, stop, step)
