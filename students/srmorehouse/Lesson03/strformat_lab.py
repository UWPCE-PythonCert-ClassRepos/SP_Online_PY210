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
def rewrite (in_tuple):
    length = len ( in_tuple)
    format_string = 'the {:d} numbers are:'.format(length)
    for i in range(length):
        format_string += ' {:d}'
        if i < length-1:
            format_string += ','
    return format_string.format(*in_tuple)

"""
Task Four

Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
Hint: use index numbers to specify positions.
"""
def reformat (seq):
    return ('0{:d} {:d} {:d} 0{:d} {:d}'.format(seq[3], seq[4], seq[2], seq[0], seq[1]))

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
    return (f'The weight of an {seq[0].upper()} is {seq[1]*1.2} and the weight of a {seq[2].upper()} is {seq[3]*1.2}')

"""
Task Six

Write some Python code to print a table of several rows, each with a name,
an age and a cost. Make sure some of the costs are in the hundreds and
thousands to test your alignment specifiers.  And for an extra task,
given a tuple with 10 consecutive numbers, can you work how to quickly
print the tuple in columns that are 5 charaters wide? It can be done on one short line!
"""
def print_table ():
    align = '{:^10}'
    print (align.format('name1') + align.format('5') + align.format('$99.01'))
    print (align.format('name2') + align.format('10') + align.format('$1000.00'))
    print (align.format('name3') + align.format('101') + align.format('$10000'))
    print ('')

    align2 = '{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}'
    print(align2.format('10', '11', '12', '13', '14', '15', '16', '17', '18', '19'))


if __name__ == "__main__":

    t = ( 2, 123.4567, 10000, 12345.67)
    t1 = (0, 1)
    t2 = (1,2,3,4,5,6,7,8,9)
    four_element_tuple = (4, 30, 2017, 2, 27)
    four_element_list = ['oranges', 1.3, 'lemons', 1.1]

    print (' Task One')
    print (reformat_seq (t))
    print ('\n Task Two')
    print (redo_reformat_seq (t))
    print ('\n Task Three Test 1')
    print (rewrite (t1))
    print ('\n Task Three Test 2')
    print (rewrite (t2))
    print ('\n Task Four')
    print (reformat (four_element_tuple))
    print ('\n Task Five')
    print (fstring (four_element_list))
    print ('\n Task Six')
    print (print_table ())

