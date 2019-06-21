#!/usr/bin/env python3

#task 1
lab_tuple = (2, 123.4567, 10000, 12345.67)
print("file_{:03d}:  {:.2f}, {:.2e}, {:.2e}".format(lab_tuple[0],lab_tuple[1],lab_tuple[2],lab_tuple[3]))

#task 2
file_name = lab_tuple[0]
first_num = lab_tuple[1]
second_num = lab_tuple[2]
third_num = lab_tuple[3]

print(f'file_{file_name:03d}:  {first_num:.2f}, {second_num:.2e}, {third_num:.2e}')

#task 3 - maybe update str(len(t)) to be formatted as well
def formatter(t):
    strings = "{:d}, " * (len(t)-1) + "{:d}"
    return 'The ' + str(len(t)) + ' numbers are: ' + strings.format(*t)

assert formatter((1,2,3)) == 'The 3 numbers are: 1, 2, 3'
assert formatter((1,2,3,4,5)) == 'The 5 numbers are: 1, 2, 3, 4, 5'

#task 4
task4_tuple = (4, 30, 2017, 2, 27)
print(f'{task4_tuple[3]:02d} {task4_tuple[-1]} {task4_tuple[2]} {task4_tuple[0]:02d} {task4_tuple[1]}')

#task 5
task5_tuple = ('oranges', 1.3, 'lemons', 1.1)
def remove_plural(word):
    return word[:-1]

print(f'The weight of an {remove_plural(task5_tuple[0])} is {task5_tuple[1]} and the weight of a {remove_plural(task5_tuple[2])} is {task5_tuple[3]}')
print(f'The weight of an {remove_plural(task5_tuple[0].upper())} is {task5_tuple[1]*1.2} and the weight of a {remove_plural(task5_tuple[2].upper())} is {task5_tuple[3]*1.2}')

#task 6
table = ['Bob', 32, 999.99,
        'Sarah', 45, 2000,
        'Banjo', 99, 10.10]

def print_table(t):
    strings = ("{:<10}{:<10}{:<10}" + '\n') * (int(len(t)/3)-1) + "{:<10}{:<10}{:<10}"
    print(strings.format(*t))

print_table(table)
