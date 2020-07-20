"""
Purpose: Lessen 3 homework one python certificate from UW
Author: Pirouz Naghavi
Date: 06/26/2020
"""

# Imports
import copy
from collections import Sequence
import unittest


def check_sequence(seq, minlength):
    """"This function checks to see if the sequence is a sequence and has the right length.

        Args:
            seq: Is the sequence passed to the function to check.
            minlength: Is the minimum length required.

        Raises:
            ValueError: If length of sequence is less than minlength.
            TypeError: If None is passed instead of sequence.
                If seq is not of type collection.Sequence.
        """

    if seq is None:
        raise TypeError('Sequence is None.')
    if not isinstance(seq, Sequence):
        raise TypeError('Sequence is not a member of collections.Sequence.')
    if len(seq) < minlength:
        raise ValueError('Minimum length of sequence is {}.'.format(minlength))


def exchange_first_last(seq):
    """"This function swaps first element and last element of list.

    Args:
        seq: Is the sequence passed to the function to swap first and last element of.

    Returns:
        A shallow copy of sequence where the first and last elements are exchanged.

    Raises:
        ValueError: If length of sequence is less than one.
        TypeError: If None is passed instead of sequence.
            If seq is not of type collection.Sequence.
    """
    # Protecting against bad inputs
    check_sequence(seq, 1)

    # Creating a shallow copy of the sequence.
    # new_seq = lis(seq) would work the same way as a shallow copy
    new_seq = seq[:]

    # Sequence length one needs to be handled separately
    if len(new_seq) == 1:
        return new_seq

    # Creating memory placeholders for for first and last elements
    first = new_seq[0: 1]
    last = new_seq[len(seq)-1: len(seq)]

    # Returning corrected sequence
    return last + new_seq[1: len(new_seq) - 1] + first


def exchange_first_last_deep(seq):
    """"This function swaps first element and last element of list.

    Args:
        seq: Is the sequence passed to the function to swap first and last element of.

    Returns:
        A deep copy of sequence where the first and last elements are exchanged.

    Raises:
        ValueError: If length of sequence is less than one.
        TypeError: If None is passed instead of sequence.
            If seq is not of type collection.Sequence.
    """

    # Protecting against bad inputs
    check_sequence(seq, 1)

    # Creating a shallow copy of the sequence
    new_seq = copy.deepcopy(seq)

    # Sequence length one needs to be handled separately
    if len(new_seq) == 1:
        return new_seq

    # Creating memory placeholders for for first and last elements
    first = new_seq[0: 1]
    last = new_seq[len(seq)-1: len(seq)]

    # Returning corrected sequence
    return last + new_seq[1: len(new_seq) - 1] + first


def alternate_item_deep(seq):
    """"This function removes every other item starting with first element.

    Args:
        seq: Is the sequence passed to the function to remove every other item.

    Returns:
        A deep copy of sequence where every other item is removed.

    Raises:
        ValueError: If length of sequence is less than one.
        TypeError: If None is passed instead of sequence.
            If seq is not of type collection.Sequence.
    """

    # Protecting against bad inputs
    check_sequence(seq, 1)

    # Creating a shallow copy of the sequence
    new_seq = copy.deepcopy(seq)

    # Retuning alternate series
    return new_seq[:: 2]


def normalized_alternate_item_deep(seq):
    """"This function removes every other item with first four and last four.

    Args:
        seq: Is the sequence passed to the function to remove every other item with first
            four and last four items.

    Returns:
       A deep copy of sequence where every other item with first four and last four items
           are removed.

    Raises:
        ValueError: If length of sequence is less than one.
        TypeError: If None is passed instead of sequence.
            If seq is not of type collection.Sequence.
    """

    # Protecting against bad inputs
    check_sequence(seq, 1)

    # Creating a shallow copy of the sequence
    new_seq = copy.deepcopy(seq)

    # Retuning normalized alternate series. First four and last four items are removed.
    return new_seq[4: len(new_seq) - 4: 2]


def reverse_deep(seq):
    """"This function reverses a sequence.

    Args:
        seq: Is the sequence passed to the function to reverse.

    Returns:
        A deep copy of sequence in reverse order.

    Raises:
        ValueError: If length of sequence is less than one.
        TypeError: If None is passed instead of sequence.
            If seq is not of type collection.Sequence.
    """

    # Protecting against bad inputs
    check_sequence(seq, 1)

    # Creating a shallow copy of the sequence
    new_seq = copy.deepcopy(seq)

    # Retuning reverses series
    return new_seq[:: -1]


def thirds_last_first_middle_deep(seq):
    """"This function returns the sequence in a new order.

    This function returns the sequence in a new order where the last third is first then
    first third then middle third.

    Args:
        seq: Is the sequence passed to the function to order.

    Returns:
      A deep copy of sequence in a new order where the last third is first then first
          third then middle third.

    Raises:
        ValueError: If length of sequence is less than three.
        TypeError: If None is passed instead of sequence.
            If seq is not of type collection.Sequence.
    """

    # Protecting against bad inputs
    check_sequence(seq, 3)

    # Creating a shallow copy of the sequence
    new_seq = copy.deepcopy(seq)

    # Retuning alternate series
    return new_seq[2 * len(new_seq) // 3: len(new_seq)] + new_seq[: len(new_seq) // 3]\
        + new_seq[len(new_seq) // 3: 2 * len(new_seq) // 3]


class TestSlicing(unittest.TestCase):

    def test_exchange_first_last(self):

        # List tests
        self.assertEqual(exchange_first_last([1]), [1])
        self.assertEqual(exchange_first_last([1, 2]), [2, 1])
        self.assertEqual(exchange_first_last([1, 2, 3]), [3, 2, 1])
        self.assertEqual(exchange_first_last([1, 2, 3, 4]), [4, 2, 3, 1])
        exchange_first_last_range_100 = list(range(100))
        exchange_first_last_range_100[0] = 99
        exchange_first_last_range_100[99] = 0
        self.assertEqual(exchange_first_last(list(range(100))), exchange_first_last_range_100)

        # Tuple tests
        self.assertEqual(exchange_first_last((1, 1)), (1, 1))
        self.assertEqual(exchange_first_last((1, 2)), (2, 1))
        self.assertEqual(exchange_first_last((1, 2, 3)), (3, 2, 1))
        self.assertEqual(exchange_first_last((1, 2, 3, 4)), (4, 2, 3, 1))
        self.assertEqual(exchange_first_last((1, 2, 3, 4, 5, 6, 7, 8, 9)), (9, 2, 3, 4, 5, 6, 7, 8, 1))

        # String tests
        self.assertEqual(exchange_first_last('1'), '1')
        self.assertEqual(exchange_first_last('12'), '21')
        self.assertEqual(exchange_first_last('123'), '321')
        self.assertEqual(exchange_first_last('1234'), '4231')
        self.assertEqual(exchange_first_last('1234567891011121314151617181920'), '0234567891011121314151617181921')

        # Exception tests
        self.assertRaisesRegex(TypeError, 'Sequence is None.', exchange_first_last, None)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , exchange_first_last, {1, 2, 3})
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , exchange_first_last, (1))
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , exchange_first_last, 88)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , exchange_first_last, copy)
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', exchange_first_last, [])
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', exchange_first_last, ())
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', exchange_first_last, '')

    def test_exchange_first_last_deep(self):

        # List tests
        self.assertEqual(exchange_first_last_deep([1]), [1])
        self.assertEqual(exchange_first_last_deep([1, 2]), [2, 1])
        self.assertEqual(exchange_first_last_deep([1, 2, 3]), [3, 2, 1])
        self.assertEqual(exchange_first_last_deep([1, 2, 3, 4]), [4, 2, 3, 1])
        exchange_first_last_range_100 = list(range(100))
        exchange_first_last_range_100[0] = 99
        exchange_first_last_range_100[99] = 0
        self.assertEqual(exchange_first_last_deep(list(range(100))), exchange_first_last_range_100)
        self.assertEqual(exchange_first_last_deep([[1]]), [[1]])
        self.assertEqual(exchange_first_last_deep([[1], [2]]), [[2], [1]])
        self.assertEqual(exchange_first_last_deep([[1], [2], [3]]), [[3], [2], [1]])
        self.assertEqual(exchange_first_last_deep([[1, 2], 3, 4]), [4, 3, [1, 2]])
        self.assertEqual(exchange_first_last_deep([[1, 3], 3, 4]), [4, 3, [1, 3]])
        input_list = [1, 2, 3, [1, 2, 3, [1, 2]]]
        self.assertEqual(exchange_first_last_deep(input_list[3]), [[1, 2], 2, 3, 1])
        self.assertEqual(input_list, [1, 2, 3, [1, 2, 3, [1, 2]]])

        # Tuple tests
        self.assertEqual(exchange_first_last_deep((1, 1)), (1, 1))
        self.assertEqual(exchange_first_last_deep((1, 2)), (2, 1))
        self.assertEqual(exchange_first_last_deep((1, 2, 3)), (3, 2, 1))
        self.assertEqual(exchange_first_last_deep((1, 2, 3, 4)), (4, 2, 3, 1))
        self.assertEqual(exchange_first_last_deep((1, 2, 3, 4, 5, 6, 7, 8, 9)), (9, 2, 3, 4, 5, 6, 7, 8, 1))

        # String tests
        self.assertEqual(exchange_first_last_deep('1'), '1')
        self.assertEqual(exchange_first_last_deep('12'), '21')
        self.assertEqual(exchange_first_last_deep('123'), '321')
        self.assertEqual(exchange_first_last_deep('1234'), '4231')
        self.assertEqual(exchange_first_last_deep('1234567891011121314151617181920'), '0234567891011121314151617181921')

        # Exception tests
        self.assertRaisesRegex(TypeError, 'Sequence is None.', exchange_first_last_deep, None)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , exchange_first_last_deep, {1, 2, 3})
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , exchange_first_last_deep, (1))
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , exchange_first_last_deep, 88)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , exchange_first_last_deep, copy)
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', exchange_first_last_deep, [])
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', exchange_first_last_deep, ())
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', exchange_first_last_deep, '')

    def test_alternate_item_deep(self):

        # List tests
        self.assertEqual(alternate_item_deep([1]), [1])
        self.assertEqual(alternate_item_deep([1, 2]), [1])
        self.assertEqual(alternate_item_deep([1, 2, 3]), [1, 3])
        self.assertEqual(alternate_item_deep([1, 2, 3, 4]), [1, 3])
        exchange_first_last_range_100 = list(range(100))
        self.assertEqual(alternate_item_deep(list(range(100))), exchange_first_last_range_100[:: 2])
        input_list = [1, 2, [1, 2, 3, [1, 2]], 3]
        self.assertEqual(alternate_item_deep(input_list[2]), [1, 3])
        self.assertEqual(alternate_item_deep(input_list), [1, [1, 2, 3, [1, 2]]])
        self.assertEqual(input_list, [1, 2, [1, 2, 3, [1, 2]], 3])

        # Tuple tests
        self.assertEqual(alternate_item_deep((1, 1)), (1, ))
        self.assertEqual(alternate_item_deep((1, 2)), (1, ))
        self.assertEqual(alternate_item_deep((1, 2, 3)), (1, 3))
        self.assertEqual(alternate_item_deep((1, 2, 3, 4)), (1, 3))
        self.assertEqual(alternate_item_deep((1, 2, 3, 4, 5, 6, 7, 8, 9)), (1, 3, 5, 7, 9))

        # String tests
        self.assertEqual(alternate_item_deep('1'), '1')
        self.assertEqual(alternate_item_deep('12'), '1')
        self.assertEqual(alternate_item_deep('123'), '13')
        self.assertEqual(alternate_item_deep('1234'), '13')
        self.assertEqual(alternate_item_deep('1234567891011121314151617181920'), '1357901234567890')

        # Exception tests
        self.assertRaisesRegex(TypeError, 'Sequence is None.', alternate_item_deep, None)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , alternate_item_deep, {1, 2, 3})
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , alternate_item_deep, (1))
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , alternate_item_deep, 88)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , alternate_item_deep, copy)
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', alternate_item_deep, [])
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', alternate_item_deep, ())
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', alternate_item_deep, '')

    def test_normalized_alternate_item_deep(self):

        # List tests
        self.assertEqual(normalized_alternate_item_deep([1]), [])
        self.assertEqual(normalized_alternate_item_deep([1, 2]), [])
        self.assertEqual(normalized_alternate_item_deep([1, 2, 3, 4, 5, 6]), [])
        self.assertEqual(normalized_alternate_item_deep([1, 2, 3, 4, 5, 6, 7]), [])
        self.assertEqual(normalized_alternate_item_deep([1, 2, 3, 4, 5, 6, 7, 8]), [])
        self.assertEqual(normalized_alternate_item_deep([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), [5, 7, 9])
        self.assertEqual(normalized_alternate_item_deep([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), [5, 7, 9])
        exchange_first_last_range_100 = list(range(100))
        self.assertEqual(normalized_alternate_item_deep(list(range(100))), exchange_first_last_range_100[4: 96: 2])
        input_list = [1, 2, 3, 4, [1, 2, 3, [1, 2]], 11, 12, 13, 14]
        self.assertEqual(normalized_alternate_item_deep(input_list[4]), [])
        self.assertEqual(normalized_alternate_item_deep(input_list), [[1, 2, 3, [1, 2]]])
        self.assertEqual(input_list, [1, 2, 3, 4, [1, 2, 3, [1, 2]], 11, 12, 13, 14])

        # Tuple tests
        self.assertEqual(normalized_alternate_item_deep((1, )), ())
        self.assertEqual(normalized_alternate_item_deep((1, 2)), ())
        self.assertEqual(normalized_alternate_item_deep((1, 2, 3, 4, 5, 6)), ())
        self.assertEqual(normalized_alternate_item_deep((1, 2, 3, 4, 5, 6, 7)), ())
        self.assertEqual(normalized_alternate_item_deep((1, 2, 3, 4, 5, 6, 7, 8)), ())
        self.assertEqual(normalized_alternate_item_deep((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)), (5, 7, 9))
        self.assertEqual(normalized_alternate_item_deep((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)), (5, 7, 9))
        input_list = (1, 2, 3, 4, (1, 2, 3, (1, 2)), 11, 12, 13, 14)
        self.assertEqual(normalized_alternate_item_deep(input_list[4]), ())
        self.assertEqual(normalized_alternate_item_deep(input_list), ((1, 2, 3, (1, 2)), ))
        self.assertEqual(input_list, (1, 2, 3, 4, (1, 2, 3, (1, 2)), 11, 12, 13, 14))

        # String tests
        self.assertEqual(normalized_alternate_item_deep('1'), '')
        self.assertEqual(normalized_alternate_item_deep('12'), '')
        self.assertEqual(normalized_alternate_item_deep('123456'), '')
        self.assertEqual(normalized_alternate_item_deep('1234567'), '')
        self.assertEqual(normalized_alternate_item_deep('12345678'), '')
        self.assertEqual(normalized_alternate_item_deep('xxxx56789xxxx'), ('579'))
        self.assertEqual(normalized_alternate_item_deep('xxxx56789xxxxx'), ('579'))

        # Exception tests
        self.assertRaisesRegex(TypeError, 'Sequence is None.', normalized_alternate_item_deep, None)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , normalized_alternate_item_deep, {1, 2, 3})
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , normalized_alternate_item_deep, (1))
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , normalized_alternate_item_deep, 88)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , normalized_alternate_item_deep, copy)
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', normalized_alternate_item_deep, [])
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', normalized_alternate_item_deep, ())
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', normalized_alternate_item_deep, '')

    def test_reverse_deep(self):

        # List tests
        self.assertEqual(reverse_deep([1]), [1])
        self.assertEqual(reverse_deep([1, 2]), [2, 1])
        self.assertEqual(reverse_deep([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])
        self.assertEqual(reverse_deep([1, 2, 3, 4, 5, 6, 7]), [7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(reverse_deep([1, 2, 3, 4, 5, 6, 7, 8]), [8, 7, 6, 5, 4, 3, 2, 1])
        temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        temp_list.reverse()
        self.assertEqual(reverse_deep([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), temp_list)
        exchange_first_last_range_100 = list(range(100))
        exchange_first_last_range_100.reverse()
        self.assertEqual(reverse_deep(list(range(100))), exchange_first_last_range_100)
        input_list = [1, 2, 3, 4, [1, 2, 3, [1, 2]], 11, 12, 13, 14]
        self.assertEqual(reverse_deep(input_list[4]), [[1, 2], 3, 2, 1])
        self.assertEqual(reverse_deep(input_list), [14, 13, 12, 11, [1, 2, 3, [1, 2]], 4, 3, 2, 1])
        self.assertEqual(input_list, [1, 2, 3, 4, [1, 2, 3, [1, 2]], 11, 12, 13, 14])

        # Tuple tests
        self.assertEqual(reverse_deep((1,)), (1,))
        self.assertEqual(reverse_deep((1, 2)), (2, 1))
        self.assertEqual(reverse_deep((1, 2, 3, 4, 5, 6)), (6, 5, 4, 3, 2, 1))
        self.assertEqual(reverse_deep((1, 2, 3, 4, 5, 6, 7)), (7, 6, 5, 4, 3, 2, 1))
        self.assertEqual(reverse_deep((1, 2, 3, 4, 5, 6, 7, 8)), (8, 7, 6, 5, 4, 3, 2, 1))
        input_list = (1, 2, 3, 4, (1, 2, 3, (1, 2)), 11, 12, 13, 14)
        self.assertEqual(reverse_deep(input_list[4]), ((1, 2), 3, 2, 1), )
        self.assertEqual(reverse_deep(input_list), (14, 13, 12, 11, (1, 2, 3, (1, 2)), 4, 3, 2, 1))
        self.assertEqual(input_list, (1, 2, 3, 4, (1, 2, 3, (1, 2)), 11, 12, 13, 14))

        # String tests
        self.assertEqual(reverse_deep('1'), '1')
        self.assertEqual(reverse_deep('12'), '21')
        self.assertEqual(reverse_deep('123456'), '654321')
        self.assertEqual(reverse_deep('1234567'), '7654321')
        self.assertEqual(reverse_deep('12345678'), '87654321')
        self.assertEqual(reverse_deep('xxxx56789xxxx'), ('xxxx98765xxxx'))
        self.assertEqual(reverse_deep('xxxx56789xxxxx'), ('xxxxx98765xxxx'))

        # Exception tests
        self.assertRaisesRegex(TypeError, 'Sequence is None.', reverse_deep, None)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , reverse_deep, {1, 2, 3})
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , reverse_deep, (1))
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , reverse_deep, 88)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , reverse_deep, copy)
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', reverse_deep, [])
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', reverse_deep, ())
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 1.', reverse_deep, '')

    def test_thirds_last_first_middle_deep(self):

        # List tests
        self.assertEqual(thirds_last_first_middle_deep([1, 2, 3]), [3, 1, 2])
        self.assertEqual(thirds_last_first_middle_deep([1, 2, 3, 4]), [3, 4, 1, 2])
        self.assertEqual(thirds_last_first_middle_deep([1, 2, 3, 4, 5]), [4, 5, 1, 2, 3])
        self.assertEqual(thirds_last_first_middle_deep([1, 2, 3, 4, 5, 6]), [5, 6, 1, 2, 3, 4])
        self.assertEqual(thirds_last_first_middle_deep([1, 2, 3, 4, 5, 6, 7]), [5, 6, 7, 1, 2, 3, 4])
        self.assertEqual(thirds_last_first_middle_deep([1, 2, 3, 4, 5, 6, 7, 8]), [6, 7, 8, 1, 2, 3, 4, 5])
        temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(thirds_last_first_middle_deep([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
                         [9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8])
        input_list = [1, 2, 3, 4, [1, 2, 3, [1, 2]], 11, 12, 13, 14]
        self.assertEqual(thirds_last_first_middle_deep(input_list[4]), [3, [1, 2], 1, 2])
        self.assertEqual(thirds_last_first_middle_deep(input_list), [12, 13, 14, 1, 2, 3, 4, [1, 2, 3, [1, 2]], 11])
        self.assertEqual(input_list, [1, 2, 3, 4, [1, 2, 3, [1, 2]], 11, 12, 13, 14])

        # Tuple tests
        self.assertEqual(thirds_last_first_middle_deep((1, 2, 3)), (3, 1, 2))
        self.assertEqual(thirds_last_first_middle_deep((1, 2, 3, 4)), (3, 4, 1, 2))
        self.assertEqual(thirds_last_first_middle_deep((1, 2, 3, 4, 5)), (4, 5, 1, 2, 3))
        self.assertEqual(thirds_last_first_middle_deep((1, 2, 3, 4, 5, 6)), (5, 6, 1, 2, 3, 4))
        self.assertEqual(thirds_last_first_middle_deep((1, 2, 3, 4, 5, 6, 7)), (5, 6, 7, 1, 2, 3, 4))
        self.assertEqual(thirds_last_first_middle_deep((1, 2, 3, 4, 5, 6, 7, 8)), (6, 7, 8, 1, 2, 3, 4, 5))
        temp_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
        self.assertEqual(thirds_last_first_middle_deep((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)),
                         (9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8))
        input_list = (1, 2, 3, 4, (1, 2, 3, (1, 2)), 11, 12, 13, 14)
        self.assertEqual(thirds_last_first_middle_deep(input_list[4]), (3, (1, 2), 1, 2))
        self.assertEqual(thirds_last_first_middle_deep(input_list), (12, 13, 14, 1, 2, 3, 4, (1, 2, 3, (1, 2)), 11))
        self.assertEqual(input_list, (1, 2, 3, 4, (1, 2, 3, (1, 2)), 11, 12, 13, 14))

        # String tests
        self.assertEqual(thirds_last_first_middle_deep('123'), '312')
        self.assertEqual(thirds_last_first_middle_deep('1234'), '3412')
        self.assertEqual(thirds_last_first_middle_deep('12345'), '45123')
        self.assertEqual(thirds_last_first_middle_deep('123456'), '561234')
        self.assertEqual(thirds_last_first_middle_deep('1234567'), '5671234')
        self.assertEqual(thirds_last_first_middle_deep('12345678'), '67812345')

        # Exception tests
        self.assertRaisesRegex(TypeError, 'Sequence is None.', thirds_last_first_middle_deep, None)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , thirds_last_first_middle_deep, {1, 2, 3})
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , thirds_last_first_middle_deep, (1))
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , thirds_last_first_middle_deep, 88)
        self.assertRaises(TypeError, 'Sequence is not a member of collections.Sequence.'
                          , thirds_last_first_middle_deep, copy)
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 3.', thirds_last_first_middle_deep, [1])
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 3.', thirds_last_first_middle_deep, (1, 2))
        self.assertRaisesRegex(ValueError, 'Minimum length of sequence is 3.', thirds_last_first_middle_deep, '')


if __name__ == "__main__":
    # run some unit tests on everything
    unittest.main()
