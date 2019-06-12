#!/usr/bin/env python3

# Sparse array class (1D)
# Only store non-zero values, use dictionary with key=index, value=value
# Want to provide functionality to make it seem like a real array
#  Length method should return total length (with zeros)
#  Should support getting and setting
#  Should support deletion by arbitrary index
#  Should support append
#  Should return error if accessed beyond end
#  Try and support slicing (return indices between endpoints, filling in zeros as needed)

class SparseArray(object):
    def __init__(self, input_array):
        # Store length (this will change if values are appended or deleted)
        self.length = len(input_array)
        # Initialize dict and fill with values
        self.value_dict = {}
        for index, value in enumerate(input_array):
            self.store_value(index, value)

    # Create a separate method for assignment in case storage method changes
    def store_value(self, index, value):
        if value: # Only store non-zero items
            self.value_dict[index] = value

    def __len__(self):
        return self.length

    def append(self, value):
        if value: # If non-zero, add value at next position
            self.value_dict[self.length] = value
            self.length += 1 # Increase 'virtual' length

    def __contains__(self, item):
        return item in self.value_dict.values()

    def __getitem__(self, index):
        if isinstance(index,slice): # slice
            array_slice = []
            # Set step to 1 if not defined
            if index.step == 0:
                raise ValueError('slice step cannot be zero')
            step = index.step if index.step else 1
            # Populate slice from array
            # Continue as long as current index is valid
            if step > 0:
                start, stop = index.start, index.stop
                current = start
                while current < self.length and current < stop:
                    value = self.value_dict.get(current,0)
                    array_slice.append(value)
                    current += step
            elif step < 0:
                start, stop = index.stop, index.start
                current = stop
                while current >= 0 and current > start:
                    value = self.value_dict.get(current,0)
                    array_slice.append(value)
                    current += step
            return array_slice
        elif isinstance(index,int): # single index
            if index >= self.length:
                raise IndexError('list index out of range')
            else:
                # Return zero if not in dictionary
                return self.value_dict.get(index,0)

    def __setitem__(self, index, value):
        if index >= self.length:
            raise IndexError('list assignment index out of range')
        else:
            self.store_value(index, value)

    def __delitem__(self, index):
        if index >= self.length:
            raise IndexError('list assignment index out of range')
        else:
            if index in self.value_dict:
                del self.value_dict[index]
