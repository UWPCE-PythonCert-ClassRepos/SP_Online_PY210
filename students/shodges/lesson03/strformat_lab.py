#!/usr/bin/env python3

#task 1
values = (2, 123.4567, 10000, 12345.67)
print('file_{:03d} :   {:.2f}, {:.2e}, {:.2e}'.format(*values))

#task 2
print(f"file_{values[0]:03d} :   {values[1]:.2f}, {values[2]:.2e}, {values[3]:.2e}")

#task 3
def formatter(nums):
    l = len(nums)

    return ('The {:d} numbers are: ' + ', '.join(['{:d}']*l)).format(l, *nums)

#task 4
date = (4, 30, 2017, 2, 27)
print('{3:02d} {4} {2} {0:02d} {1}'.format(*date))

#task 5
thelist = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {thelist[0][:-1]} is {thelist[1]} and the weight of a {thelist[2][:-1]} is {thelist[3]}")

print(f"The weight of an {thelist[0][:-1].upper()} is {thelist[1]*1.2} and the weight of a {thelist[2][:-1].upper()} is {thelist[3]*1.2}")

#task 6
values = [['Apple', 27, 1.67], ['Orange', 12, 2.99], ['Banana', 37, .67], ['Broccoli', 4, 4.99], ['Cheese', 1067, 18.99], ['Boat', 10670, 5099.87], ['House', 102478, 106070.42]]

for value in values:
    print('{:15} {:6d}         ${:10.2f}'.format(*value))

#extra tasks
consecutive_tuple = (1,2,3,4,5,6,7,8,9,10)
print((' '.join(['{:5d}']*len(consecutive_tuple))).format(*consecutive_tuple))
