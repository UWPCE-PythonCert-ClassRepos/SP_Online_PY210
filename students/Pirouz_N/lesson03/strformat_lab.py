#!/usr/bin/env python3
"""
Purpose: Lessen 3 homework three, string formatting lab, python certificate from UW
Author: Pirouz Naghavi
Date: 07/02/2020
"""

# imports
import random
import string

# Task One
print('Task one:')

input_tuple = (2, 123.4567, 10000, 12345.67)

# Printing results of converting input_tuple to: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print('file_{} :   {:.2f}, {:.2e}, {:.3g}'
      .format(format(input_tuple[0], '0>3'), input_tuple[1], input_tuple[2], input_tuple[3]))

# Task two
print('Task two:')

# Using f strings
print(f'file_{format(input_tuple[0], "0>3")} :   {input_tuple[1]:.2f}, {input_tuple[2]:.2e}, {input_tuple[3]:.3g}')

# Task three
print('Task three:')

input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print('Using format string:')
print('The {} numbers are: {}'.format(len(input_tuple), '{:d}, ' * (len(input_tuple) - 1) + '{:d}')
      .format(*input_tuple))

print('Using f string:')
print(f'The {len(input_tuple)} numbers are: { str(input_tuple)[1:len(str(input_tuple))-1]}')


def formatter(nums):
    """"This function string with length and elements in nums.

        Args:
            nums: Is the index that the fibonacci sequence will be generated until and the value of index
                n will be returned.

        Returns:
            String including length and values inside of nums.

        Raises:
            ValueError: If nums is a None.
            TypeError: If nums isn't a tuple.
        """

    if nums is None:
        raise ValueError('Tuple cannot be None.')
    if not isinstance(nums, tuple):
        raise TypeError('Input must be of type tuple.')
    return f'The {len(nums)} numbers are: { str(nums)[1:len(str(nums))-1]}'


print('Using formatter function:')
print(formatter(input_tuple))

# Task four
print('Task four:')

input_tuple = (4, 30, 2017, 2, 27)
print(input_tuple[4])

# Using string formatting to print '02 27 2017 04 30'
print('Results:  {} {} {} {} {}'.format(format(input_tuple[3], '0>2'),
                                        input_tuple[4], input_tuple[2], format(input_tuple[0], '0>2'), input_tuple[1]))
print('Expected: 02 27 2017 04 30')

# Task five
print('Task five:')

input_list = ['oranges', 1.3, 'lemons', 1.1]

# Printing expected string using f string "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
print(f'The weight of an {input_list[0][:len(input_list[0]) - 1]} is {input_list[1]} and the weight of a'
      f' {input_list[2][:len(input_list[2]) - 1]} is {input_list[3]}')

# Printing expected result for comparison
print('Which is the same as:')
print("The weight of an orange is 1.3 and the weight of a lemon is 1.1")

# Printing updated result string using f string "The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32"
print('Next part:')
print(f'The weight of an {input_list[0][:len(input_list[0]) - 1].upper()} is {1.2 * input_list[1]} and the weight of a'
      f' {input_list[2][:len(input_list[2]) - 1].upper()} is {1.2 * input_list[3]}')

# Printing expected result for comparison
print('Which is the same as:')
print("The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32")

# Task six
print('Task six:')

# Printing table
print('{:<20.20s}\t{:<20.20s}\t{:<20.20s}\t{:<20.20s}'.format('First Name', 'Last Name', 'Age', 'Cost'))
print('____________________________________________________________________________________________')

# Generating a table
for _ in range(50):
    # Generating data randomly length of each field is limited to 20 characters
    print('{:<20.20s}\t{:<20.20s}\t{:<20.20s}\t{:<20.20s}'
          .format(''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 100))).title(),
                  ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 100))).title(),
                  str(random.randint(1, 100)), str(random.randint(1, 100000000000000000000))))

# Task 6 extra task
print('Task six extra:')
input_tuple = tuple([str(i) for i in range(1000, 1010)])
print('The {} numbers are: \n{}'.format(len(input_tuple), '{:<5.5s}\t' * (len(input_tuple))).format(*input_tuple))

