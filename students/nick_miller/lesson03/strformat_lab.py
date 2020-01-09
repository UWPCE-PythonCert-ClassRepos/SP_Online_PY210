#!/usr/bin/env python3

"""PY210_SP - 3.3 - strformat_lab
author: Nick Miller"""

# Task 01

tuple1 = (2, 123.4567, 10000, 12345.67)

# produce: 'file_002 :   123.46, 1.00e+04, 1.23e+04'

"""
1. The first element is used to generate a filename that can help with file sorting. The idea behind the “file_002”
is that if you have a bunch of files that you want to name with numbers that can be sorted, you need to “pad” the
numbers with zeros to get the right sort order.
2. The second element is a floating point number. You should display it with 2 decimal places shown.
3. The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal
places shown.
4. The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.
"""


print("file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(*tuple1))
print()

# Task 02

"""
Using your results from Task One, repeat the exercise, but this time using an alternate type of format string
(hint: think about alternative ways to use .format() (keywords anyone?),
and also consider f-strings if you’ve not used them already).
"""

print(f"file_{tuple1[0]:03d} :   {tuple1[1]:.2f}, {tuple1[2]:.2e}, {tuple1[3]:.2e}")
print()

# or

print("file_{:03d} : {:8.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67))
print()

# Task 03

"""
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary number of values.
Hint: You can pass in a tuple of values to a function with a *:
"""


def formatter(inTuple):
    """print out arbitrary length tuples"""
    tcounter = "the {} numbers are: ".format(len(inTuple))
    if len(inTuple) > 0:
        tcounter += "{}".format(inTuple[0])
    for num in inTuple[1:]:
        tcounter += ", {}".format(num)
    return tcounter


testTuple = (1, 2, 3, 4, 5, 6, 7, 8)

print(formatter(testTuple))
print()

# Task 04

"""
Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formatting to print:
'02 27 2017 04 30'
Hint: use index numbers to specify positions.
"""

tupleshuffle = (4, 30, 2017, 2, 27)

