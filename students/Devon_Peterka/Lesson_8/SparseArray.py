#!/usr/bin/env python3

class SparseArray:
    def __init__(self, input):
        '''
        Saves the length of the original object and truncates zeroes and
        stores remaining values into memory.
        '''
        self._len = len(input)
        self.save = self.packit(input)
        del input
 
    def __len__(self):
        '''
        returns the length of the original, non-compressed, array.
        '''
        return self._len

    def __getitem__(self, index):
        '''
        returns value of array at a desired index.  Can take index,
        slice, or tuple inputs - tuple input is read as:
        (start, stop, step)
        '''
        if isinstance(index, int):
            self.check_index(index)
            return self.save[index] if index in self.save.keys() else 0
        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            self.check_index(start)
            self.check_index(stop)
            return [self[i] for i in range(start, stop, step)]
        elif isintance(index, tuple):
            # Can interpret tuple inputs by assuming the start, stop, step format.  Breaks down if more than (3) value tuple.
            if len(index) in range(0,4):
                start = index[0]
                stop = None if len(index) < 2 else index[1]
                step = None if len(index) < 3 else index[2]
                return [self[i] for i in range(start, stop, step)]
            else:
                raise NotImplementedError ('Invalid tuple index')


    def __setitem__(self, index, value):
        '''
        Sets sparse array indices with user inputs.
        '''
        # First check if index is valid.
        self.check_index(index)

        # Now alter the array accordingly
        if value != 0: self.save.update({index:value})
        else:
            new_array[i] = [self.save[i] if i in self.save.keys() else 0 for i in range(self._len)]

    def __delitem__(self, index):
        '''
        Deletes values from array.  Called with the 'del' command.
        '''
        # Verify index is within array
        self.check_index(index)
        
        # Make copy of array and delete desired instance
        temp_array = list(self)
        del temp_array[index]
        
        # Save temp_array into sparse array format
        self._len = len(temp_array)
        self.save = self.packit(temp_array)
        
        # Clean-up
        del temp_array
        
    def __str__(self):
        '''
        Returns full sparse array for viewing.
        '''
        return f'{[0 if i not in self.save.keys() else self.save[i] for i in range(self._len)]}'

    def __repr__(self):
        '''
        Prints a non-cryptic representation of the object.
        '''
        return f'SparseArray({[0 if i not in self.save.keys() else self.save[i] for i in range(self._len)]})'

    def packit(self, input):
        '''
        Stores only non-zero values and their indices in a dictionary.
        '''
        return {i: input[i] for i in range(self._len) if input[i] != 0}

    def check_index(self, index):
        '''
        Validates a user-input index values.
        '''
        if index not in range(0, self._len):
            raise IndexError(f'Index {index} out of range.  Must '
                             f'be between, 0 and {self._len - 1}, '
                              'inclusive')

    def append(self, input):
        '''
        Add additional terms to existing sparse array.
        '''
        # Copy full un-truncated array and append with new inputs
        temp_array = list(self)
        temp_array += input
        
        # Record new array length and compress array into dictionary
        self._len = len(temp_array)
        self.save = self.packit(temp_array)
        
        # Clean-up
        del temp_array
