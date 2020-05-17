#!/usr/bin/env python3

#task one
task_one_string = 'file_{:0>3} :  {:.2f}, {:.2e}, {:.3g}'
input_tuple = ( 2, 123.4567, 10000, 12345.67)

print(task_one_string.format(*input_tuple))

#task two
task_two_string = 'file_{file_name:0>3} :  {file_attr_1:.2f}, {file_attr_2:.2e}, {file_attr_3:.3g}'
print(task_two_string.format(file_name=2, file_attr_1 = 123.456, file_attr_2 = 10000, file_attr_3 = 12345.67))

#task three
def formatter(in_tuple):
    l = len(in_tuple)
    format_string = ', '.join(['{:d}']*l)
    format_string = 'the {} numbers are: ' + format_string
    return format_string.format(l,*in_tuple)

#task four
input_tuple =  ( 4, 30, 2017, 2, 27)
format_string = '{3:02d} {4} {2} {0:02d} {1}'
print(format_string.format(*input_tuple))

#task five
input_list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {input_list[0][:-1].upper()} is {input_list[1]*1.2:.1f} and the weight of a {input_list[2][:-1].upper()} is {input_list[3]*1.2:.1f}')

#task six
'''
Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide? It can be done on one short line!
'''
input_table = [ ['kris', 37, 10],
                ['yiling', 37, 100],
                ['chase', 36, 1000],
                ['torey', 34, 10000],
                ['lina', 82, 100000]]
format_string = '{:>10} {:>3} {:>6d}'
print('      name age   cost')
for i in input_table:
    print(format_string.format(i[0],i[1],i[2]))

#task extra
input_tuple = list(range(995,1005))
print("\n".join(["{:>5}"]*len(input_tuple)).format(*input_tuple))