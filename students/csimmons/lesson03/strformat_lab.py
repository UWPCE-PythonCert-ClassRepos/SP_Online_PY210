#!/usr/bin/env python3
# Craig Simmons
# Python 210
# strformat_lab: String Formatting Exercises
# Created 11/22/2020 - csimmons

# Task 1
# Transform ( 2, 123.4567, 10000, 12345.67) to 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print('\nTask One Excercise: Use str.format()')
tuple1 = ( 2, 123.4567, 10000, 12345.67)
print("file_{0:0>3d}, {1:.2f}, {2:.2e}, {3:.2e}".format(*tuple1))

# Task 2
# Format above tuple using alt format string type 
print('\nTask Two Excercise: Use f-string syntax')
tuple1 = ( 2, 123.4567, 10000, 12345.67)
print(f'file_{tuple1[0]:0>3d}, {tuple1[1]:.2f}, {tuple1[2]:.2e}, {tuple1[3]:.2e}')

# Task 3
# Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to accept arbitrary # of values
print('\nTask Three Excercise: Dynamically accept any # of values')
numbers1 = ( 1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers2 = ( 10, 20, 30, 40)

def test(seq):
    replacer = '{:d}, '
    make_fstring = 'The {:d} numbers are: ' + (replacer * len(seq))
    full = '"' + make_fstring[:-2] + '."'
    print(full.format(len(seq), *seq))
test(numbers1)
test(numbers2)

# Task 4
# Given a 5 element tuple: ( 4, 30, 2017, 2, 27), print: '02 27 2017 04 30'
print('\nTask Four Excercises: format numeric tuple, adjust # positions')
datetime = ( 4, 30, 2017, 2, 27) 
print('string.format():    ' + "{3:0>2d} {4:d} {2:d} {0:0>2d} {1:d}".format(*datetime))
print('fstring:    ' + f"{datetime[3]:0>2d} {datetime[4]:d} {datetime[2]:d} {datetime[0]:0>2d} {datetime[1]:d}")

# Task 5
# Given this list ['oranges', 1.3, 'lemons', 1.1] write an fstring for:
# "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
print('\nTask Five Excercises: f-string fruits and weights')
fruits = ['oranges', 1.3, 'lemons', 1.1]
text_1 = "The weight of an "
text_2 = "and the weight of a "
# fstring formatting. Take plural of fruit and make singular
f1_str = f"{fruits[0].replace('s', '')} is {fruits[1]:.1f} "
f2_str = f"{fruits[2].replace('s', '')} is {fruits[3]:.1f}"
print(text_1 + f1_str + text_2 + f2_str)

# Change f-string to display fruit name in uppercase and 20% higher weight
mod = 1.2
f3_str = f"{(fruits[0].upper()).replace('S', '')} is {(fruits[1] * mod):.1f} "
f4_str = f"{(fruits[2].upper()).replace('S', '')} is {(fruits[3]* mod):.1f} "
print(text_1 + f3_str + text_2 + f4_str)

# Task 6
# Write some Python code to print a table of several rows, each with a name, an age and a cost. 
# Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
print('\nTask Six Excercises: Print data in table and format extra task')
table_data = (['Kevin', 'Simmons', 49, 20.56], ['Bruce', 'Vercingetorix', 3, 256], 
['Matt', 'Francis', 100, 1005.50], ['Randy', 'Taber', 34, 35000.89])
row = "| {fname:<8s} | {lname:<15s} | {age:<5d} | ${price:<10,.2f} |".format
for data in table_data:
    print(row(fname=data[0], lname=data[1], age=data[2], price=data[3]))

# And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly 
# print the tuple in columns that are 5 charaters wide? It can be done on one short line!
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
single_row = "\n" + ("|{:^5d}" * len(numbers)).format(*numbers)
print(single_row + "|\n")
