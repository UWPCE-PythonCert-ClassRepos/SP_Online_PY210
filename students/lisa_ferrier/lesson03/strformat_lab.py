#!/usr/bin/env python
# strformat_lab.py
# Lisa Ferrier, Python 210, Lesson 3


# task one
# format items in a list as specified
# [0] should read 'file' + up to 3 char padding
# [1] returns a float with two decimals.
# [2] returns an int in scientific notation with 2 decimals.
# [3] returns a float with many digits in scientific notation with 3 decimals.
ls = (2, 123.4567, 10000, 12345.67)
ls = 'file{0:0>3} :  {1:.2f}, {2:.2e}, {3:0.2e}'.format(*ls)
print(ls)


# task two
# reformat task one using a different approach. I chose an f-string.
ls = (2, 123.4567, 10000, 12345.67)
print(f'file{ls[0]:0>3} : {ls[1]:.2f}, {ls[2]:.2e}, {ls[3]:0.2e}')


# task three
# given a tuple of abitrary length, return formatted values.
def formatter(ls):
    lsLength = len(ls)
    fstring = ('the {} numbers are: ' + ', '.join(['{:d}'] * lsLength)).format(lsLength, *ls)
    return fstring.format(*ls)


ls = (1, 2, 3, 4, 5)
formatter(ls)


# task four
# reorder and format a list of values.
t = (4, 30, 2017, 2, 27)
format_t = '{3:02}, {4:02}, {2:04}, {0:02}, {1:02}'.format(*t)
print(format_t)


# task five
# given a list (ls), format the items in the list to display their name and weight *1.2
ls = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {ls[0][:-1]} is {ls[1]*1.2} and the weight of a {ls[2][:-1]} is {ls[3]*1.2}.')


# task six
# format items in a list (ls) to display items in a consistently spaced table format.
ls = [['katarina', 3, '$64'], ['stephanie', 12, '$2.89'], ['christopher', 83, '$10100.75'], ['lola', 34, '$1050.99']]
for i in ls:
    print('{:15} {:3} {: >15}'.format(*i))

# extra task
# given a tuple (t), set the 5 char spacing between each item.
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(('{:5}' * (len(t))).format(*t))
