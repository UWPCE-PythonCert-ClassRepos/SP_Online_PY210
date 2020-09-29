#!/usr/bin/env python3
"""
Purpose: Sparse Array python certificate from UW
Author: Pirouz Naghavi
Date: 07/13/2020
"""

# imports
from collections.abc import Sequence
import operator


class SparseArray:
    """Sparse Array is data structure for spare data.

    The list hold information describing the HTML element as well as a class attribute describing the HTML tag
    called tag. It also contains instance attributes such as contents which is a list that contains the contents.
    It is very likely that the contents could include element which would be the sub elements to the current
    element. There are two major methods append and render. Append adds more contents to the contents list. Render
    adds the current element.

    Attributes:
        date: This attribute contains all the values in the data including zeros.
        """

    def __init__(self, init_data=None, dim=None):
        """Initialises the Sparse Array class.

        Args:
            init_data: Is the initializing data. If it is not provided empty structure will be created. This
                value will be a sparse array of objects or 2 sparse array of objects. In case of a 2D sparse
                array of object every row need not to have the same length additional zeros will be
                automatically added. If init_data is not sequence it will be treated as an object set for index
                zero of the data.
            dim: Dimensionality of the array.
        Raises:
            ValueError: If dim is specified as two dimensional but it is not a Sequence.

        """
        self._data = {}
        self._num_row = 0
        self._num_col = 0
        self._dim = dim if dim is not None and (dim == 1 or dim == 2) else 1
        if init_data is not None:
            if isinstance(init_data, Sequence):
                if len(init_data) != 0:
                    self._initial_sequence_update(init_data)
            else:
                self._data[0] = init_data

    def _initial_sequence_update(self, init_data):
        """Initialises the Sparse Array class when initial data is a sequence.

        Args:
            init_data: Is the initializing data. If it is not provided empty structure will be created. This
                value will be a sparse array of objects or 2 sparse array of objects. In case of a 2D sparse
                array of object every row need not to have the same length additional zeros will be
                automatically added. If init_data is not sequence it will be treated as an object set for index
                zero of the data.
        Raises:
            ValueError: If dim is specified as two dimensional but it is not a Sequence.
        """
        self._num_row = len(init_data)
        for i, row_val in enumerate(init_data):
            if self._dim == 1:
                if row_val != 0 and row_val != 0.0 and row_val != '':
                    self._data[i] = row_val
            else:
                self._num_col = len(row_val) if len(row_val) > self._num_col else self._num_col
                try:
                    for j, col_val in enumerate(row_val):
                        if col_val != 0 and col_val != 0.0 and col_val != '':
                            self._data[(i, j)] = col_val
                except ValueError as err:
                    raise ValueError("Every row of initial data must be a sequence." + str(err))

    @property
    def data(self):
        """It returns array slice based on the passed slice and value. This will return a row.

        Returns:
             The property of data as a form of list of lists.
        """
        if self._dim == 2:
            return [[self._data[(i, j)] if (i, j) in self._data else 0 for j in range(self._num_col)]
                    for i in range(self._num_row)]
        else:
            return [self._data[i] if i in self._data else 0 for i in range(self._num_row)]

    @data.setter
    def data(self, init_data):
        """Resets the Sparse Array class from blank with initial data.

        Args:
            init_data: Is the initializing data. If it is not provided empty structure will be created. This
                value will be a sparse array of objects or 2 sparse array of objects. In case of a 2D sparse
                array of object every row need not to have the same length additional zeros will be
                automatically added. If init_data is not sequence it will be treated as an object set for index
                zero of the data.
            dim: Dimensionality of the array.
        Raises:
            ValueError: If dim is specified as two dimensional but it is not a Sequence.
        """
        self._data = {}
        self._num_row = 0
        self._num_col = 0
        self._dim = dim if dim is not None and (dim == 1 or dim == 2) else 1
        if init_data is not None:
            if isinstance(init_data, Sequence):
                if len(init_data) != 0:
                    self._initial_sequence_update(init_data)
            else:
                self._data[0] = init_data

    @staticmethod
    def _slice_range(slc, length):
        return range(operator.index(slc.start) if slc.start is not None else 0,
                     operator.index(slc.stop) if slc.stop is not None else length,
                     operator.index(slc.step) if slc.step is not None else 1)

    def _two_d_tuple_get_item_both_slice(self, item):
        """It returns an array slice based on the passed slice tuple. This will return a list of lists.

        Args:
            item: Slice tuple that needs to be returned.

        Returns:
             This will return a list of lists based on the tuple of slices.
        """
        return [[self._data[(i, j)] if (i, j) in self._data else 0
                 for j in self._slice_range(item[1], self._num_col)]
                for i in self._slice_range(item[0], self._num_row)]

    def _two_d_tuple_get_item_one_slice(self, item):
        """It returns an array slice based on the passed slice and value. This will return a row.

        Args:
            item: Slice and value that needs to be returned.

        Returns:
             This will return a row as a list based on the slice and value.
        """
        return [[self._data[(i, j)] if (i, j) in self._data else 0
                 for j in self._slice_range(item[1], self._num_col)]
                for i in range(operator.index(item[0]), operator.index(item[0]) + 1)]

    def _two_d_tuple_get_item_two_slice(self, item):
        """It returns an array slice based on the passed slice and value. This will return a column vector.

        Args:
            item: Slice and value that needs to be returned.

        Returns:
             This will return a column vector as a list of list based on the slice and value.
        """
        return [[self._data[(i, j)] if (i, j) in self._data else 0
                 for j in range(operator.index(item[1]), operator.index(item[1]) + 1)]
                for i in self._slice_range(item[0], self._num_row)]

    def _two_d_tuple_get_item_no_slice(self, item):
        """It returns array slice based on the passed slice and value. This a value located at provided index.

        Args:
            item: Index tuple that needs to be returned.

        Returns:
             This will return a value based on the tuple of values.
        """
        return self._data[(operator.index(item[0]), operator.index(item[1]))] \
            if (operator.index(item[0]), operator.index(item[1])) in self._data else 0

    def _two_d_tuple_get_item(self, item):
        """It returns an array slice based on the passed tuple. This a value located at provided index tuple.

        Args:
            item: Index or slice tuple that needs to be returned.

        Returns:
             This will return a value, row, column vector, or matrix based on the tuple of values.
        """
        if len(item) == 2:
            if isinstance(item[0], slice) and isinstance(item[1], slice):
                return self._two_d_tuple_get_item_both_slice(item)
            elif isinstance(item[0], slice) and not isinstance(item[1], slice):
                return self._two_d_tuple_get_item_two_slice(item)
            elif not isinstance(item[0], slice) and isinstance(item[1], slice):
                return self._two_d_tuple_get_item_one_slice(item)
            else:
                return self._two_d_tuple_get_item_no_slice(item)
        else:
            raise IndexError("Dimension tuple for two array must be two dimensional")

    def _two_d_get_item(self, item):
        """It returns an array slice based on the passed tuple, slice, or value. This a value located at index tuple.

        Args:
            item: Index or slice tuple that needs to be returned.

        Returns:
             This will return a value, row, column vector, or matrix based on the tuple of values.
        """
        if isinstance(item, tuple):
            return self._two_d_tuple_get_item(item)
        elif isinstance(item, slice):
            return [[self._data[(i, j)] if (i, j) in self._data else 0 for j in range(self._num_col)]
                    for i in self._slice_range(item[0], self._num_row)]
        else:
            return[[self._data[(i, j)] if (i, j) in self._data else 0
                    for j in range(self._num_col)]
                   for i in range(operator.index(item), operator.index(item) + 1)]

    def _one_d_get_item(self, item):
        """It returns an array slice based on the passed slice, or value. This is located at index or slice.

        Args:
            item: Index or slice that needs to be returned.

        Returns:
             This will return a value, or list based on slice or value.
        """
        if isinstance(item, slice):
            return [self._data[i] if i in self._data else 0
                    for i in self._slice_range(item[0], self._num_row)]
        else:
            return self._data[operator.index(item)] if operator.index(item) in self._data else 0

    def __getitem__(self, item):
        """It returns an array slice based on the passed slice, or value for 1D and 2D.

        Args:
            item: Index or slice or as tuple of indexes or slices combo that needs to be returned for 1D or 2D.

        Returns:
             This will return a value, list, list of list as vector, or list of lists as matrix based on item.

        Raises:
            TypeError: When values are not operator.index convertible to ints.
            IndexError: When index of values are out of bounds.
        """
        try:
            if self._dim == 2:
                return self._two_d_get_item(item)
            else:
                return self._one_d_get_item(item)
        except TypeError as err:
            raise TypeError("Indices must be integers." + str(err))
        except IndexError as err:
            raise IndexError("Provided index is out of bounds of the data." + str(err))

    def _set_two_d(self, item, value):
        """It sets a value at a certain tuple for 2D.

        Args:
            item: Index tuple that the value needs to be placed into.
            value: That needs to be placed in the index tuple.

        Raises:
            TypeError: When values are not operator.index convertible to ints.
            IndexError: When index of values are out of bounds.
        """
        if isinstance(item, tuple):
            if len(item) == 2:
                self._num_row = operator.index(item[0]) + 1 if self._num_row - 1 < operator.index(item[0]) \
                    else self._num_row
                self._num_col = operator.index(item[1]) + 1 if self._num_col - 1 < operator.index(item[1]) \
                    else self._num_col
                self._data[(operator.index(item[0]), operator.index(item[1]))] = value
            else:
                raise IndexError("2D array requires a tuple of indices with length of two.")
        else:
            raise IndexError("2D array requires a tuple of indices.")

    def _set_one_d(self, item, value):
        """It sets a value at a certain index for 1D.

        Args:
            item: Index that the value needs to be placed into.
            value: That needs to be placed in the index.

        Raises:
            TypeError: When values are not operator.index convertible to ints.
            IndexError: When index of values are out of bounds.
        """
        self._num_row = operator.index(item) + 1 if self._num_row - 1 < operator.index(item) \
            else self._num_row
        self._data[operator.index(item)] = value

    def __setitem__(self, item, value):
        """It sets a value at a certain index for 1D or index tuple for 2D.

        Args:
            item: Index or index tuple that the value needs to be placed into.
            value: That needs to be placed in the index or index tuple.

        Raises:
            TypeError: When values are not operator.index convertible to ints.
            IndexError: When index of values are out of bounds.
        """
        try:
            if self._dim == 2:
                self._set_two_d(item, value)
            else:
                self._set_one_d(item, value)
        except TypeError as err:
            raise TypeError("Indices must be integers." + str(err))
        except IndexError as err:
            raise IndexError("Provided index is out of bounds of the data." + str(err))

    def __len__(self):
        """It the length of the current instance."""
        if self._dim == 2:
            return self._num_row
        else:
            return self._num_row

    @property
    def shape(self):
        """It the shape of the current instance."""
        if self._dim == 2:
            return self._num_row, self._num_col
        else:
            return self._num_row

    def _delitem_two_d(self, key):
        """It removes item at key for 2D."""
        if isinstance(key, tuple) and len(key) == 2:
            del self._data[key]
            self._num_row = max(self._data)[0] + 1 if self._num_row - 1 == operator.index(key[0]) \
                else self._num_row
            self._num_col = max(self._data, key=lambda x: x[1])[1] + 1 if self._num_col - 1 == operator.index(key[1]) \
                else self._num_col
        else:
            raise IndexError("The item for 2D array must be a tuple of length 2.")

    def _delitem_one_d(self, key):
        """It removes item at key for 1D."""
        del self._data[key]
        self._num_row = max(self._data) + 1 if self._num_row - 1 == operator.index(key) \
            else self._num_row

    def __delitem__(self, key):
        """It removes item at key. For 2D keys must be tuples of length 2. For 1D an integer value should suffice."""
        try:
            if self._dim == 2:
                self._delitem_two_d(key)
            else:
                self._delitem_one_d(key)
        except TypeError as err:
            raise TypeError("Indices must be integers." + str(err))
        except IndexError as err:
            raise IndexError("Provided index is out of bounds of the data." + str(err))

    @staticmethod
    def _print_two_d_item(data, index, start, end_short, end_long):
        """Prints item of sparse 2D array."""
        obj_str = ""
        obj_str += start
        if len(data[index]) < 15:
            obj_str += str(data[index]) + end_short
        else:
            obj_str += '[' + str(data[index][0]) + ', ' + str(data[index][1]) + ', ' + str(
                data[index][2]) + ', ..., ' \
                       + str(data[index][len(data[index]) - 3]) + ', ' + str(
                data[index][len(data[index]) - 2]) + ', ' \
                       + str(data[index][len(data[index]) - 1])
            obj_str += end_long
        return obj_str

    def _str_two_d(self, all_data):
        """Prints data of sparse 2D array."""
        obj_str = ''
        if self._num_row == 0:
            obj_str += "{}D Sparse Array ([".format(self._dim) + '[]' + '])'
        elif self._num_row == 1:
            obj_str += "{}D Sparse Array ([".format(self._dim) + str(all_data[0]) + '])'
        else:
            obj_str += self._print_two_d_item(all_data, 0, "{}D Sparse Array ([", ',\n', '],\n')
            for i in range(1, self._num_row - 1):
                obj_str += self._print_two_d_item(all_data, i, "                  ", ',\n', '],\n')
            obj_str += self._print_two_d_item(all_data, self._num_row - 1, "                  ", '])', ']])')
        return obj_str

    def __str__(self):
        """Prints data of sparse array."""
        all_data = self.data
        if self._dim == 2:
            return self._str_two_d(all_data)
        else:
            return "{}D Sparse Array (".format(self._dim) + str(all_data) + ')'


if __name__ == "__main__":
    """blank = SparseArray()
    blank[0] = 100
    blank[1] = 100
    blank[100] = 1000
    blank[1000] = 1
    print(blank)
    print(len(blank))
    del blank[1000]
    print(blank)
    print(len(blank))
    two_d_blank = SparseArray(dim=2)
    two_d_blank[1, 100] = 100
    two_d_blank[0, 0] = 100
    two_d_blank[2, 5] = 'better than numpy! lol'
    print(two_d_blank)
    del two_d_blank[2, 5]
    print(two_d_blank)
    one_d_init = SparseArray([1, 2, 3, 4, 5, 6])
    one_d_init[20] = 100
    one_d_init[200] = 'better than numpy! lol'
    print(one_d_init)
    del one_d_init[200]
    print(one_d_init)

    two_d_init = SparseArray([[1, 2, 3, 4, 5, 6]], dim=2)
    print(two_d_init)
    two_d_init[100, 100] = 'I am "cool"'
    print(two_d_init)
    print(two_d_init.shape)
    print(two_d_init[1, 1])
    print(two_d_init[99:, 100])
    two_d_init[52, 52] = 'I am "cool"'
    print(two_d_init[50:59, 50:59])
    print(SparseArray(two_d_init[50:59, 50:59], dim=2))"""