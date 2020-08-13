#!/usr/bin/env python3

'''
Task 1
    Write a format string to take the tuple (2, 123.4567, 1000, 1234.67)
    and produce 'file_002 :  123.46, 1.00e+04, 1.23e+04'

Task 2
    Repeat Task 1 but this time use an alternate type of format string.
    consider using f-strings.

Task 3
    Rewrite, "the 3 numbers are: {:d}, {:d}, {:d}",format(1,2,3) to take
    arbitrary values - and an arbitrary number of values.  Allow it to be
    a string called by either a literal or by a name.

Task 4
    Given a (5) element tuple (4, 30, 2017, 2, 27) use string formatting
    to print '02 27 2017 04 30'

Task 5
    Given the list ['oranges', 1.3, 'lemons', 1.1]
    write an f-string that will display, "The weight of an orange is 1.3 and
    the weight of a lemon is 1.1"
    Now see if you can change the names to uppercase and make the weight 20% 
    higher for each.

Task 6
   Write a python code to print a table of several rows, each with a name
   and age, and a cost.  Make sure some of the costs are in the hudreds
   and thousands to test your alignment.
   
   And for an extra task, given a tuple with (10) consecutive numbers, 
   can you work how to quickly print the tuple in columns that are (5) 
   characters wide?  HINT: Make it a one-liner.
'''

#Task 1
in_data = ( 2, 123.4567, 10000, 12345.67)
out1 = 'file {:0>3d} : {:.2f}, {:.2e}, {:.2e}'.format(*in_data)
print(out1)

#Task 2
print(f'file {in_data[0]:0>3d} : {in_data[1]:.2f}, {in_data[2]:.2e}, {in_data[3]:.2e}')

#Task 3
def formatter(in_tuple):
    return ('The ' + str(len(in_tuple)) +' numbers are ' + (len(in_tuple)-1)*'{}, ' + '{}').format(*in_tuple)
print(formatter((1, 2, 3)))
print(formatter((1, 8, 14, 22, 6, -208)))

#Task 4
in_tuple = (4, 30, 2017, 2, 27)
print('{3:0>2d} {4:0>2d} {2} {0:0>2d} {1:0>2d}'.format(*in_tuple))

#Task 5
List = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {List[0][:-1]} is {List[1]} and the weight of a {List[2][:-1]} is {List[3]}')    # used double indices to truncate the 's'
print(f'The weight of an {List[0][:-1].upper()} is {List[1] * 1.2} and the weight of a {List[2][:-1].upper()} is {List[3] * 1.2}')

#Task 6
List_Data = [["Bill", 53, 1.95],    # name, age, and $ data as a list of lists.
    ["Joe", 4, 82.151258],    # Format below can handle partial cents
    ["Amy", 37, 1047.85],
    ["Jackie", 15, 203212.8735],    # Format below can handle up to the $100,000's
    ["Nick", 37, 0]]
print(f'\n|{"NAME":20} {"AGE":3} :  {"PAYOUT":>11} |')    # formatted header row
for i, info in enumerate(List_Data):    #enumerate to separate indices from content lists of List_Data.  Will only use content lists
    print(f'|{info[0]:.<20}.{info[1]:.>3d} : $ {info[2]:>10,.2f} |')

#Task 6 - Extra
print(('|{:^5d}' * 10).format(*tuple(range(100,110))) + '|')
