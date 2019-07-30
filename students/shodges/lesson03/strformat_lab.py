#!/usr/bin/env python3

#task 1
values = (2, 123.4567, 10000, 12345.67)
print('file_{:03d} :   {:.2f}, {:.2e}, {:.2e}'.format(*values))

#task 2

#task 3
def formatter(nums):
    l = len(nums)

    return ('The {:d} numbers are: ' + ', '.join(['{:d}']*l)).format(l, *nums)
