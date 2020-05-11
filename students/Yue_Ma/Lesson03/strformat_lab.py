#!/usr/bin/env python3

# Task 1
tuple_raw = (2, 123.4567, 10000, 12345.67)
result_1 = "file_{:03d}: {:.2f}, {:.2e}, {:.2e}".format(*tuple_raw)
print(result_1)

# Task 2
result_2 = f"file_{tuple_raw[0]:0>3d}: {tuple_raw[1]:.2f}, {tuple_raw[2]:.2e}, {tuple_raw[3]:.2e}"
print(result_2)

# Task 3


def formatter(in_tuple):
    result_3 = ("the {} numbers are: " + "{}, " * len(in_tuple)).format(len(in_tuple), *in_tuple)
    return result_3[:-2]


print(formatter((2, 3, 5, 10)))

# Task 4
tuple_4 = (4, 30, 2017, 2, 27)
result_4 = f'{tuple_4[3]:0>2d} {tuple_4[4]} {tuple_4[2]} {tuple_4[0]:0>2d} {tuple_4[1]}'
print(result_4)

# Task 5
list_5 = ['oranges', 1.3, 'lemons', 1.1]
n = list_5[1] * 1.2
m = list_5[3] * 1.2
result_5_1 = f"The weight of an {list_5[0][:-1]} is {list_5[1]} and " \
           f"the weight of a {list_5[2][:-1]} is {list_5[2]}"
result_5_2 = f"The weight of an {list_5[0][:-1].upper()} is {n} " \
             f"and the weight of a {list_5[2][:-1].upper()} is {m}"
print(result_5_1)
print(result_5_2)

# Task 6
list_6 = (('Yue', 25, '$66.6'), ('Yanan', 25, '$1000000'), ('Jack', 65, '$442423'))
for item in list_6:
    result_6 = '{:<10}{:<10}{:<10}'.format(*item)
    print(result_6)

# Extra Task
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
format_string = '{:=5}' * len(numbers)
print(format_string.format(*numbers)[4:])

