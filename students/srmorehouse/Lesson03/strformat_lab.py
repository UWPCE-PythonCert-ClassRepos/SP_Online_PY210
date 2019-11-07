#!/usr/bin/env python3

"""
Steve Morehouse
Lesson 03

"""

"""
Task One
Write a format string that will take the following four element tuple
( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'

"""
def reformat_seq (seq):
    return ('file_{:03d} :   {:.2f}, {:.2e}, {:.2e}'.format(*seq))

"""
Task Two

Using your results from Task One, repeat the exercise, but this time
using an alternate type of format string (hint: think about alternative
ways to use .format() (keywords anyone?), and also consider f-strings
if you’ve not used them already).
"""
def redo_reformat_seq (seq):
    return (f'file_{seq[0]:03d} :   {seq[1]:.2f}, {seq[2]:.2e}, {seq[3]:.2e}')

"""
Task Three

Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

to take an arbitrary number of values.
"""
def rewrite (seq):
    none

"""
Task Four

Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
Hint: use index numbers to specify positions.
"""
def reformat (seq):
    none

"""
Task Five
Here’s a task for you: Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1
Now see if you can change the f-string so that it displays the
names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
"""
def fstring (seq):
    none

"""
Task Six

Write some Python code to print a table of several rows, each with a name,
an age and a cost. Make sure some of the costs are in the hundreds and
thousands to test your alignment specifiers.  And for an extra task,
given a tuple with 10 consecutive numbers, can you work how to quickly
print the tuple in columns that are 5 charaters wide? It can be done on one short line!
"""
def print_table (x):
    none


if __name__ == "__main__":

    t = ( 2, 123.4567, 10000, 12345.67)
    print (reformat_seq (t))
    print (redo_reformat_seq (t))
