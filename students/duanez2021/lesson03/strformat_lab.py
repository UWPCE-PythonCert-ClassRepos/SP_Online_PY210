#!/usr/bin/env python3
import sys
##############################################################
# 20200620    djm list lab series 4
#
# Duane McCollum Python self-paced winter 2020
#
# String Formatting Exercise
#  given ( 2, 123.4567, 10000, 12345.67)
#  create a format string to output
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'
# #
#############################################################

# Task One
t = (2, 123.4567, 10000, 12345.67)
#out_text= "file_00{}:  {:.2f}, {:.2e},  {:.2e}".format(t[0], t[1], t[2], t[3])
out_text= "file_{:03d} :  {:.2f}, {:.2e},  {:.2e}".format(t[0], t[1], t[2], t[3])
out_text= "file_{:03d} :  {:.2f}, {:.2e},  {:.2e}".format(*t)
print(out_text)


# task two
print ('file_'f'{t[0]:03d}'': 'f'{t[1]:.2f}', ', ' f'{t[2]:.2e}', ', ' f'{t[3]:.2e}')

# task Three
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
#  to take an arbitrary number of values.

def formatter(t):
    out_string=''
    for i, j in enumerate(t):
        out_string += '{:d},'
    return (out_string[:len(out_string)-1])

# range of #s 1 to 100
print (formatter(range(101)[1:]).format(*range(101)[1:]))


# task four
# Given a 5 element tuple:
# ( 4, 30, 2017, 2, 27)
# use string formating to print:
# '02 27 2017 04 30'
#

t = (4, 30, 2017, 2, 27)
print (f'{t[3]:02d}', f'{t[4]:d}', f'{t[2]:d}', f'{t[0]:02d}', f'{t[1]:d}',sep=' ')


# task five

# Here’s a task for you: Given the following four element list:
# ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display:
#  The weight of an orange is 1.3 and the weight of a lemon is 1.1
x = ['oranges', 1.3, 'lemons', 1.1]

print ('The weight of an ' f'{x[0][:-1]:s}' ' is ' f'{x[1]:.1f}' 
       ' and the weight of a ' f'{x[2][:-1]:s}' ' is ' f'{x[3]:.1f}')

#Now see if you can change the f-string so that it displays
# the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).

print ('The weight of an ' f'{str(x[0][:-1]).upper():s}' ' is ' f'{(x[1])*1.2:.1f}' 
       ' and the weight of a ' f'{str(x[2][:-1]).upper():s}' ' is ' f'{(x[3])*1.2:.1f}')


# task 6
'{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')

# In this simple example everything aligns nicely. But that will not be the case when the numbers to the left of the
# decimal place vary. Then you will need to use alignment specifiers. Do some research on this using the links below. Then:
#
#       my notes
#       xt=('Orange', 20, 20000000.00)
#       '{:20}{:10}{:20.2f}'.format(*xt)
#       '${:,.2f}'.format(1234.5)
#       '{:<10}'  ' {:<10}${:12,.2f}'.format(*xt)
#
#       '{:{align}{width}}'.format('test', align='^', width='10')
#       '{:{align}{width}}'.format('test', align='<', width='10')
#


# Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of
#     the costs are in the hundreds and thousands to test your alignment specifiers.

xt=('Orange', 20, 200000000.00, 'Limes', 100, 1000.00, 'Dead Crabs', 1, 1.478)
def print_rows(t):
    #a row is three consecutive tuple members
    print('{:<25}'  ' {:<10}{:>15}'.format('Name', 'Age', 'Cost'))
    out_string=''
    for i, j in enumerate(t):
        out_string += str(j)
        if (i+1) % 3 == 0:
            print('{:<25}'  ' {:<10}${:>15,.2f}'.format(t[i-2], t[i-1], t[i]))
            out_string =''

print_rows(xt)


#     And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple
#     in columns that are 5 charaters wide? It can be done on one short line!

int_tuple = (13, 21, 7, 5, 27, 71, 911, 1311, 3, 1)
#one way to do this
('{:>5}'*len(int_tuple)).format(*int_tuple)
# double the size
('{:>5}'*len(int_tuple*2)).format(*int_tuple*2)
