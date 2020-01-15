#!/usr/bin/env python


class Sparse_Array:
    """Class for a 1D array which functions as a list, but does not store zero values."""
    def __init__(self, values=None):
        """Store all non-zero list values in a dict, with the indices as keys."""
        self.length = len(values)
        if values is None:
            self.values = {}
        else:
            self.values = {i: value for i, value in enumerate(values) if value != 0}
    
    def __len__(self):
        """
        Return the length of the initial input, not the stored dict.
        
        The initial input can be updated.
        """
        return self.length
    
    def __getitem__(self, query):
        """Read the input first, then retrieve a value or raise an error."""
        if isinstance(query, slice):
            keys = list(range(self.length))[query]
            return [self.values[key] if (key in self.values.keys()) else 0 for key in keys]
        elif isinstance(query, tuple):  # For use in 2D arrays.
            return 'yes tuple'
        else:
            if query > self.length:
                raise IndexError('cannot access index beyond end')
            else:
                try:
                    return self.values[query]
                except KeyError:
                    return 0
                    
    def __setitem__(self, query, value):
        """
        Depending on the input, raise an error, store a value, or delete the value & key.
        
        The virtual length remains unchanged.
        """
        if query > self.length:
            raise IndexError('cannot access index beyond end')
        elif value != 0:
            self.values[query] = value
        else:
            del self.values[query]  # Simulates storing a zero
            
    def __delitem__(self, query):
        """Delete a value & key, and shorten the length."""
        del self.values[query]
        self.length -= 1
        
    def __iter__(self):
        """Make the dict iterable."""
        return iter(self.values)
        
    def __reversed__(self):
        """Make the dict reversible."""
        return reversed(self.values)
        
    def append(self, value):
        """Make the dict appendible."""
        self.values[self.length] = value
        self.length += 1