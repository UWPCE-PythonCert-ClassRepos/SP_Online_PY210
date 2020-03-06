#!/usr/bin/env python3

#Task One
tuple = (2, 123.4567, 10000, 12345.67)

# Displays 'file_002 :  123.46, 1.00e+04, 1.23e+04'
tuple_elements = f'file_{tuple[0]:03d} : {tuple[1]:.2f}, {tuple[2]:.2e}, {tuple[3]:.2e}'
print(tuple_elements)

# Task Two
tuple = (2, 123.4567, 10000, 12345.67)

# Alternate method that displays 'file_002 :  123.46, 1.00e+04, 1.23e+04'
tuple_elements = 'file_{:03d} : {:.2f}, {:.2e}, {:.2e}'.format(*tuple)
print(tuple_elements)

# Task Three
# Rewrites "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary number of values.
def formatter(in_tuple):
    tuple_list = ', '.join(['{:d}'] * len(in_tuple))
    form_string = ('the {} numbers are: ' + tuple_list).format(len(in_tuple), *in_tuple)
    print(form_string)

formatter((1, 2, 3))
formatter((3, 9, 11, 15, 19, 65))

# Task Four
# Uses string formatting to print '02 27 2017 04 30'
def tuple_formatter(tuple):
    if len(tuple) == 5:
        tuple_elements = f'{tuple[3]:02d} {tuple[4]:2d} {tuple[2]:4d} {tuple[0]:02d} {tuple[1]:2d}'
    print(tuple_elements)

tuple_formatter((4, 30, 2017, 2, 27))

# Task Five
# Using f-string displays 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
def f_string_formatter(list):
    f_string = f'The weight of an {list[0]} is {list[1]} and the weight of a {list[2]} is {list[3]}'
    print(f_string)

f_string_formatter(['orange', 1.3, 'lemon', 1.1])

def f_string_formatter2(list):
    f_string = f'The weight of an {list[0].upper()} is {list[1] * 1.2} and the weight of a {list[2].upper()} is {list[3] * 1.2}'
    print(f_string)

f_string_formatter2(['orange', 1.3, 'lemon', 1.1])

# Task Six
# Displays a table of several rows, each with a name, an age and a cost
def table(rows):
    print('{:<10} | {:<5} | {:<10}'.format('Name', 'Age', 'Cost'))
    print('=' * 27)
    for item in range(len(rows)):
        print(f'{rows[item][0]:<10} | {rows[item][1]:<5} | ${rows[item][2]:<10}')

table([('John', 25, 2500), ('Mary', 33, 1500), ('Steven', 45, 4000), ('Josephine', 32, 2000), ('David', 39, 3000)])

# And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide? It can be done on one short line!