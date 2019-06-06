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

    def __getitem__(self, index):
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

if __name__ == "__main__":
    # Create a test array with functionality
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    print(len(test_array))
    print(test_array[9])
