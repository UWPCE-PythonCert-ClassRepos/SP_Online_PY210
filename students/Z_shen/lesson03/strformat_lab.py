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
  Write some Python code to print a table of several rows,each with a name,
  an age and a cost. Make sure some of the costs are in the hundreds and thousands
  to test your alignment specifiers.

  And for an extra task, given a tuple with 10 consecutive numbers,
  can you work how to quickly print the tuple in columns that are 5 charaters wide?
  It can be done on one short line!
'''


'''Task One'''

data=(2, 123.4567, 10000, 12345.67)

new_string='file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}'.format(*data)
print(new_string)


'''Task Two'''
print()
print(f'file_{data[0]:0>3d}: {data[1]:.2f}, {data[2]:.2e}, {data[3]:.2e}')


'''Task Three'''
print()
def formatter(in_tuple):
    form_string= 'the ' + str(len(in_tuple)) + ' numbers are :' + (len(in_tuple)-1)* '{},'+'{}'
    return form_string.format(*in_tuple)
test=( 4, 30, 2017, 2, 27)

print(formatter(test))


'''Task Four'''
print()

data4 = (4, 30, 2017, 2, 27)

print('{3:0>2d} {4} {2} {0:0>2d} {1}'.format(*data4))


'''Task Five'''
print()
list=['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {list[0][:-1]} is {list[1]} and the weight of a {list[2][:-1]} is {list[3]}')
print(f'The weight of an {list[0][:-1].upper()} is {list[1]*1.2} and the weight of a {list[2][:-1].upper()} is {list[3]*1.2}')


'''Task Six'''
print()
starters=[
    ['Andre Iguodala', 15, 300000.31456 ],
    ['Klay Thompson', 25 , 5000],
    ['Stephen Curry', 26, 6000000],
    ['Andrew Bogut', 40, 150],
]

row='| {name:15} | {age:3} | |{sign:1} {cost:<15}|'.format

print('| {:<15} | {:3} | |{:1} {:<15}|'.format('Name', 'Age', ' ', 'Cost'))
for p in starters:
    print(row(name=p[0],age=p[1],sign='$',cost=p[2]))

print(('{:<5d}'*10).format(*tuple(range(1,11))))
