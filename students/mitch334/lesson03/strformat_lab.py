"""Lesson 03 | String Formatting Exercise"""
# Goal: In this exercise we will reinforce the important concepts of string formatting, so that these start to become second nature!

"""Task 1"""
# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'

# The first element is used to generate a filename that can help with file sorting. The idea behind the “file_002”# So you need to find a string formatting operator that will “pad” the number with zeros for you.
# The second element is a floating point number. You should display it with 2 decimal places shown.
# The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.
# The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.

# unformatted_tuple = (2, 123.4567, 10000, 12345.67)
unformatted_tuple = (2, 123.4567, 10000, 12345.67)
formatted_tuple = 'file_{:03} :   {:.2f},{:.2e},{:.2e}'.format(*unformatted_tuple)
# output = "file_{:0=3} :   {}, {:.2e}, {:.2e}".format(input[0], round(input[1],2), input[2], input[3])

print(unformatted_tuple,'| unformatted')
print('file_002 :   123.46,1.00e+04,1.23e+04','| required format')
print(formatted_tuple,'| formatted TASK 2')

"""Task 2"""
# Using your results from Task One, repeat the exercise, but this time using an alternate type of format string (hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve not used them already).

formatted_tuple = f'file_{unformatted_tuple[0]:03} :   {unformatted_tuple[1]:.2f},{unformatted_tuple[2]:.2e},{unformatted_tuple[3]:.2e}'
print(formatted_tuple,'| formatted TASK 2')

"""Task 3"""
# Dynamically Building up format strings
# Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary number of values.
# Hint: You can pass in a tuple of values to a function with a *:

# Examples:
# In [20]: formatter((2,3,5))
# Out[20]: 'the 3 numbers are: 2, 3, 5'
#
# In [21]: formatter((2,3,5,7,9))
# Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'

in_tuple = (2,4,6,8,10,12,100,1,3)

def formatter(in_tuple):
    form_string = 'the '+ str(len(in_tuple)) + ' numbers are: ' + '{:d}, '*len(in_tuple)
    # print(form_string[:-2].format(*in_tuple))
    return form_string[:-2].format(*in_tuple)

print(formatter(in_tuple))

"""Task 4"""
# Given a 5 element tuple:
# ( 4, 30, 2017, 2, 27)
# use string formating to print:
# '02 27 2017 04 30'
# Hint: use index numbers to specify positions.

input_format = (4, 30, 2017, 2, 27)
output_format = '{:02} {:02} {:04} {:02} {:02}'.format(input_format[3],input_format[4],input_format[2],input_format[0],input_format[1])

print('02 27 2017 04 30 | required format')
print(output_format,'| formatted TASK 4')

"""Task 5"""
# Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1

list = ['oranges', 1.3, 'lemons', 1.1]
output = f'The weight of an {list[0][:-1]} is {list[1]} and the weight of a {list[2][:-1]} is {list[3]}'
print('The weight of an orange is 1.3 and the weight of a lemon is 1.1 | required format')
print(output, '| formatted Task 5.1')

# Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
output = f'The weight of an {list[0][:-1].upper()} is {list[1]*1.2} and the weight of a {list[2][:-1].upper()} is {list[3]*1.2}'
print(output, '| formatted Task 5.2')

"""Task 6"""
# Then you will need to use alignment specifiers. Do some research on this using the links below. Then:
# Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

table_data = [('Matthew',34.5,'$1,000')]
table_data.append (('Sara',22,'$1'))
table_data.append (('JJ',110,'$500'))
table_data.append (('Saravana',22,'$10,000'))
table_data.append (('Mitchell',22,'$120,000'))
# print(table_data)

for row in table_data:
    print(f'{row[0]:15} {round(row[1]):>3} {row[2]:>15}')

# And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide? It can be done on one short line!
consecutive_tuple = (20,21,22,23,24,25,26,27,28,29)
for item in consecutive_tuple: print(f'{item:^5}', end="")
