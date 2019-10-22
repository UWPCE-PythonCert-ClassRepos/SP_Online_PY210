# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:05:30 2019

@author: Philip Behrend
"""

tup = ( 2, 123.4567, 10000, 12345.67)

# Task 1
test_str = 'file_00{0:} :   {1:.2f}, {2:.2e}, {3:.2e}'.format(tup[0],tup[1],tup[2],tup[3])

# Task 2
test_str2 = f"file_00{tup[0]} :   {round(tup[1],2)}, {'%.2e' % tup[2]}, {'%.2e' % tup[3]}"

# Task 3
def formatter(in_tuple):
    form_string = '{:d}, '*(len(in_tuple)-1)+'{:d}'
    return ('The {} numbers are {}'.format(len(in_tuple),form_string.format(*in_tuple)))
print(formatter((1,2,3,4)))

#Task 4
test_tup = (4,30,2017,2,27)
print('{3:02d} {4:} {0:02d} {1:} {2:}'.format(*test_tup))

# Task 5
in_list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {in_list[0][:-1]} is {in_list[1]} and the weight of a {in_list[2][:-1]} is {in_list[3]}')

# Task 6
r1 = ('First', '$99.01', 'Second', '$88.09')
r2 = ('Test', '$1000.01', '2nd', '$8.09')
r3 = ('Uno', '$99999.01', 'Dos', '$808.09')
def padded(in_tuple):   
    return('{:>12}{:>12}{:>12}{:>12}'.format(*in_tuple))
print('\n',padded(r1),'\n',padded(r2),'\n',padded(r3))

