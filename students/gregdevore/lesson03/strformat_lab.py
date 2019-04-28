#!/usr/bin/env python3

def printtask(s):
    print('********')
    print('Task {:d}'.format(s))
    print('********')

tuple_to_format = (2, 123.4567, 10000, 12345.67)
print('Four element tuple to format:',tuple_to_format)

# Task One - Format four-element tuple
printtask(1)

def format_four_element_tuple(tuple_in):
    format_str = 'file_{:03d} : {:8.2f}, {:8.2e}, {:8.2e}'.format(*tuple_in)
    return format_str

print('Four element tuple using string format:')
print(format_four_element_tuple(tuple_to_format))

# Task Two - Format four element tuple alternately (with keywords)
printtask(2)

def format_four_element_tuple_keywords(tuple_in):
    format_str = 'file_{fileID:03d} : {floating:8.2f}, {integer:8.2e}, {bigfloating:8.2e}'.format(fileID=tuple_in[0],floating=tuple_in[1],integer=tuple_in[2],bigfloating=tuple_in[3])
    return format_str

print('Four element tuple using string format with keywords:')
print(format_four_element_tuple_keywords(tuple_to_format))

def format_four_element_tuple_fstring(tuple_in):
    fileID, floating, integer, bigfloating = tuple_in
    format_str = f'file_{fileID:03d} : {floating:8.2f}, {integer:8.2e}, {bigfloating:8.2e}'
    return format_str

print('Four element tuple using f-strings:')
print(format_four_element_tuple_fstring(tuple_to_format))

# Task Three - Dynamically build format string
printtask(3)

def dynamic_format_string(tuple_in):
    n = len(tuple_in)
    format_str = ('There are {:d} numbers, and they are: ' + ','.join(['{:d}'] * n)).format(n, *tuple_in)
    return format_str

tuples = [(2,3), (2,3,4), (2,3,4,5), (2,3,4,5,6)]
for tuple_to_format in tuples:
    print(dynamic_format_string(tuple_to_format))

# Task Four - String formatting with index numbers
printtask(4)

tuple_to_format = (4, 30, 2017, 2, 27)
print('Five element tuple to format:',tuple_to_format)

def format_with_index(tuple_in):
    format_str = '{3:02d} {4:02d} {2:04d} {0:02d} {1:02d}'.format(*tuple_in)
    return format_str

print('Five element tuple formatted with index:')
print(format_with_index(tuple_to_format))

# Task Five - Format string using f-strings
printtask(5)

tuple_to_format = ['oranges', 1.3, 'lemons', 1.1]
print('Tuple to format using f-strings:',tuple_to_format)

print('Tuple formatted without modification:')
fruit1, weight1, fruit2, weight2 = tuple_to_format
print(f'The weight of an {fruit1[:-1]} is {weight1} and the weight of a {fruit2[:-1]} is {weight2}')

print('Tuple formatted with upper case fruit and 20% higher weight:')
print(f'The weight of an {fruit1[:-1].upper()} is {weight1*1.2} and the weight of a {fruit2[:-1].upper()} is {weight2*1.2}')

# Task Six - Format data into columns
printtask(6)

print('Column formatting for tuple data:')
price_data = [['Chardonnay',2016,8],['Cabernet Sauvignon',2012,75],['Barbera',2005,320],['Champagne',1985,2300],['Pinot Gris',2017,20]]
for wine in price_data:
    # Left align name, right align age and price
    print('{:<20}{:>8d}{:>10.2f}'.format(*wine))

# Extra - Given a tuple with 10 consecutive numbers, print them in columns that are five characters format_with_index
print('Display tuple of consecutive numbers as 5 character columns:')
tuple_to_format = tuple(range(10))
print((''.join(['{:>5d}']*len(tuple_to_format))).format(*tuple_to_format))
