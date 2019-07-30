#!/usr/bin/env python3

#task 1
values = (2, 123.4567, 10000, 12345.67)
print('file_{:03d} :   {:.2f}, {:.2e}, {:.2e}'.format(*values))

#task 2

#task 3
def formatter(nums):
    l = len(nums)

    return ('The {:d} numbers are: ' + ', '.join(['{:d}']*l)).format(l, *nums)

#task 4
date = (4, 30, 2017, 2, 27)
print('{3:02d} {4} {2} {0:02d} {1}'.format(*date))
