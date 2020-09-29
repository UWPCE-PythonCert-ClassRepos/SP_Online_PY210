#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 11/9/2019
# strformat_lab.py

#------------------------------- Task 1 ------------------------------------------------------

my_tuple = ( 2, 123.4567, 10000, 12345.67,1)

print(f'file_{my_tuple[0]:03} :   {my_tuple[1]:.2f}, {my_tuple[2]:.2e}, {my_tuple[3]:.2e}')

#------------------------------- Task 2 ------------------------------------------------------

print('file_{:03} :   {:.2f}, {:.2e}, {:.2e}'.format(my_tuple[0], my_tuple[1], my_tuple[2], my_tuple[3]))

#------------------------------- Task 3 ------------------------------------------------------

# takes a string and loads it with an arbitrary number of values.
def formatter(in_tuple):
    size = len(in_tuple)
    
    # create string text to display the number of values found
    task_3 = 'the {} numbers are: '.format(size)

    # create tuple formatting for the number of values to display
    task_3 += ', '.join(tuple(['{:d}'] * size))

    return task_3.format(*in_tuple)
    
#------------------------------- Task 4 ------------------------------------------------------

task_4 = ( 4, 30, 2017, 2, 27)

# print task 4 in a specific order and format, with leading zeros for single digit values
print(f'{task_4[3]:02d} {task_4[4]:02d} {task_4[2]:02d} {task_4[0]:02d} {task_4[1]:02d}')

#------------------------------- Task 5 ------------------------------------------------------

task_5 = ['oranges', 1.3, 'lemons', 1.1]

# print task_5 in a specific order and format, pluralization removed
print(f'The weight of an {task_5[0][:-1]} is {task_5[1]} and the weight of a {task_5[2][:-1]} is {task_5[3]}')

# print task_5 in a specific order and format, pluralization removed, names to upper case, and add 20% to the weights
print(f'The weight of an {task_5[0][:-1].upper()} is {task_5[1]*1.2} and the weight of a {task_5[2][:-1].upper()} is {task_5[3]*1.2}')

#------------------------------- Task 6 ------------------------------------------------------

task_6 = list()
task_6.append('Name: {:<18} Age (yrs): {:>4}   cost: ${:>11,.2f}'.format('Server', 6, 10000))
task_6.append('Name: {:<18} Age (yrs): {:>4}   cost: ${:>11,.2f}'.format('Desk', 30, 600.01))
task_6.append('Name: {:<18} Age (yrs): {:>4}   cost: ${:>11,.2f}'.format('Reclining Chair', 10, 110.2))
task_6.append('Name: {:<18} Age (yrs): {:>4}   cost: ${:>11,.2f}'.format('Router', 16, 500.1))
task_6.append('Name: {:<18} Age (yrs): {:>4}   cost: ${:>11,.2f}'.format('Cell', 1, 1099.99))
task_6.append('Name: {:<18} Age (yrs): {:>4}   cost: ${:>11,.2f}'.format('Car', 100, 60000))

# Prints the list into a table
for list in task_6:
    print(list)

#------------------------------ Extra Task ----------------------------------------------------

extra_task = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print extra_task in 5 charector columns
print(''.join(tuple(['{:^5}'] * len(extra_task))).format(*extra_task))


if __name__ == "__main__":
    # run some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)  
    b_tuple = (2, 3, 5)
    c_tuple = (2, 3, 5, 7, 9)  

    assert formatter(b_tuple) == 'the 3 numbers are: 2, 3, 5'
    assert formatter(c_tuple) == 'the 5 numbers are: 2, 3, 5, 7, 9'
    assert formatter(a_tuple) == 'the 6 numbers are: 2, 54, 13, 12, 5, 32'


    print("tests passed")
