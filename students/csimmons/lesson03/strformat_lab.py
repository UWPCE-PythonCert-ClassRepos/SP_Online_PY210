#!/usr/bin/env python3
# Craig Simmons
# Python 210
# strformat_lab: String Formatting Exercises
# Created 11/22/2020 - csimmons

# Task 1
# Transform ( 2, 123.4567, 10000, 12345.67) to 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print('\nTask One Excercise: (use format())')
tuple1 = ( 2, 123.4567, 10000, 12345.67)
print("file_{0:0>3d}, {1:.2f}, {2:.2e}, {3:.2e}".format(*tuple1))

# Task 2
# Format above tuple using alt format string type 
print('\nTask Two Excercise: (use fstring syntax)')
tuple1 = ( 2, 123.4567, 10000, 12345.67)
print(f'file_{tuple1[0]:0>3d}, {tuple1[1]:.2f}, {tuple1[2]:.2e}, {tuple1[3]:.2e}')

# Task 3
# Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to accept arbitrary # of values
print('\nTask Three Excercise:')
print("the 3 numbers are: {:d}, {:d}, {:d}".format( 1, 2, 3))
seq = ( 1, 2, 3, 4, 5)
def test(seq):
    print(seq)



    
test(seq)
#def formatter(tuple_a):
 #   do_something_here_to_make_a_format_string
#   return form_string.format(*in_tuple)