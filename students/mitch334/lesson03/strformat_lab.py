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

# in_tuple = (2,4,6,8,10,12,100,1,3)
# in_tuple = (99,)

def formatter(in_tuple):
    form_string = 'the '+ str(len(in_tuple)) + ' numbers are: ' + '{:d}, '*len(in_tuple)
    # print(form_string[:-2].format(*in_tuple))
    return form_string[:-2].format(*in_tuple)
# formatter(in_tuple)
