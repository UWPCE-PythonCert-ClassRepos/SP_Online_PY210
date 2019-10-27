#!/usr/bin/env python3
# Task One
print('\n''*** Task One ***')
# used f-strings to generate the desired output instead of .format()
print(f"file_00{2} :", f"   {round(123.4567, 2)},", f"{'%.02e' % 10000},", f"{'%.02e' % 12345.67}")

# Task Two
# Used my f-string answer from task one to complete task two
print('\n''*** Task Two ***')
print(f"file_00{2} :", f"   {round(123.4567, 2)},", f"{'%.02e' % 10000},", f"{'%.02e' % 12345.67}")

filename = ['file001', 'file002', 'file010', 'file011']

a = 'cat'
b = 'dog'
c = 'parrot'
d = 'mouse'
print("the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3))
print("The story of {0}, {1}, and {c}".format(a, b, c=d))
print("My name is {0:8}".format('Fred'))

# Task 3
print('\n''*** Task Three ***')
# created a function for the task
def formatter(*in_tuple):
    numberofitems = len(in_tuple) # acquired the length of the tuple
    result = f'The {numberofitems} numbers are: {" ".join(str(x) for x in in_tuple)}' # used the len and .join with list comprehension
    return print(result)
    #return form_string.format(*in_tuple)
formatter(2, 3, 4, 9)

print('\n''*** Task Four ***')
#'02 27 2017 04 30'
formattuple = (4, 30, 2017, 2, 27) # initial tuple for the assignment
(s1, s2, s3, s4, s5) = (4, 30, 2017, 2, 27) # assigned each element in the tuple a string format location
print(f'{s4:02d}, {s5}, {s3}, {s1:02d}, {s2}') # printed the data based on location and added in :02d for decimal place data

# Task 5
print('\n''*** Task 5 ***')
#The weight of an orange is 1.3 and the weight of a lemon is 1.1
details = ['oranges', 1.3, 'lemons', 1.1] # list assigned to details
# used the index of the list to extract the data needed.
# used .rstrip('s') to make the word of each fruit singular
# used f-string to print the data
print(f"The weight of an {details[0].rstrip('s')} is {details[1]} and the weight of a {details[2].rstrip('s')} is {details[3]}")

# Task 6
print('\n''*** Task 6 ***')

# list of data for the table
table_data = ['Name:','Age:', 'Cost ($):'], ['Rick', '44', '$2324.00'], ['Steve', '46', '$3324.09'], ['Donovan', '13', '$873.30']

dash = '-' * 30 # create a separator line
for item in range(len(table_data)): # for loop based on the number of items in the table data list
    if item == 0:
        print(dash) # printing the dash
        # use f-strings to print the data
        print(f"{table_data[item][0]:<10s}{table_data[item][1]:>4s}{table_data[item][2]:>12s}")
        print(dash) # printing the dash
    else:
        # use f-strings to print the data
        print(f"{table_data[item][0]:<10s}{table_data[item][1]:>4s}{table_data[item][2]:^12s}")
