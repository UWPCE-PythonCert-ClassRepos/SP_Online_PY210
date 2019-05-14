#! /usr/bin/env python3
#Task one
print('Task One')
print('-' *30)
string_a = ( 2, 123.4567, 10000, 12345.67)
print ('file_{:0>3d}:  {:.2f} {:.2e} {:.2e}'.format(string_a[0], string_a[1], string_a[2], string_a[3]))

#Task two
string_formatter = 'the 3 numbers are: file_{:0>3d}:  {:.2f} {:.2e} {:.2e}'
print (string_formatter.format(string_a[0], string_a[1], string_a[2], string_a[3]))


#Task Three
def formatter(*seq):
    l = len(seq)
    fstring = ", ".join(["{}"]*l).format(*seq)
    return ('There {} numbers are: '.format(l) + fstring)

t = (1,2,3,4)
print(formatter(*t))

#Task Four
task_four_tuple = (4, 30, 2017, 2, 27)
a = '{:0>4d},{:0>4d},{:0>4d},{:0>4d}'.format(task_four_tuple[0],task_four_tuple[1],task_four_tuple[2],task_four_tuple[3])
print(sorted(a.split(',')))

#Task Five
a= ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of the {a[0]} is {(a[1])} and weight of {a[2]} is {a[3]}')
print(f'The weight of the {a[0].upper()} is {(a[1])*1.2} and weight of {a[2]} is {a[3]}')


#Task Six
item_string = [['item1', 41, 36.02],['item2', 22, 13.02],['item3', 2, 120.08],['item4', 64 , 234.09]]

for item in item_string:
    print ('{:<10}{:>2}{:>10}'.format(*item))

# I need help wit second part of task 6
a_tuple (1,2,3,4,5,6,7,8,9,10)



