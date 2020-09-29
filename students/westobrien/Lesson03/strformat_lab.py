#!/usr/bin/env python3

# Task 1
tuple1 = (2, 123.4567, 10000, 12345.67)

print('file_{:03d} : {:>8.2f}, {:.2e}, {:.2e} '.format(
    tuple1[0], tuple1[1], tuple1[2], tuple1[3]))


# task 2
print('file_{:03d} : {:>8.2f}, {:.2e}, {:.2e} '.format(*tuple1))

# Task 3


def formatter(in_tuple):
    tup_length = len(in_tuple)

    return ('The {:d} items are:'.format(tup_length) + ', '.join(["{:d}"] * tup_length).format(*in_tuple))

# Task 4


tuple2 = (4, 30, 2017, 2, 27)

print('{3:02d} {4} {2} {0:02d} {1}'.format(*tuple2))

# Task 5

list5 = ['oranges', 1.3, 'lemons', 1.1]

print(
    f'The weight of an {list5[0][:-1]} is {list5[1]} and the weight of a {list5[2][:-1]} is {list5[3]}')

print(
    f'The weight of an {list5[0][:-1].upper()} is {list5[1]*1.2} and the weight of a {list5[2][:-1].upper()} is {list5[3]*1.2}')

# Task 6

bob = ['Bob', 20, 1000]
cindy = ['Cindy', 25, 100000]
gary = ['Gary', 100, 4]


def alignmentFunction(in_tuple):
    return ('Name: {:>10s} Age: {:>10d} Price: {:>10d}'.format(*in_tuple))


print(alignmentFunction(bob))
print(alignmentFunction(cindy))
print(alignmentFunction(gary))
