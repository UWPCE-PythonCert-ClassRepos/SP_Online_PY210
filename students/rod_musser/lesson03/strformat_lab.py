#!/usr/bin/env python3

# Task 1
print("file_{:03d} :   {:.2f}, {:.2e}, {:.3G}"
 .format(2, 123.4567, 10000, 12345.67))
# Task 2
print("file_{file_no:03d} :   {x:.2f}, {y:.2e}, {z:.3G}"
.format(file_no=2, x=123.4567, y=10000, z=12345.67))
# Task 3
t_1 = (1, 5, 99, 12, 4, 18, 9, 11)
format_string = "the " + str(len(t_1)) + " numbers are:"
for i in range(len(t_1)):
    format_string += ' {:d}'
    if i != (len(t_1)):
        format_string += ','
print(format_string.format(*t_1))
# Task 4
t_2 = (4, 30, 2017, 2, 27)
print("{3:02d}, {4:02d}, {2}, {0:02d}, {1:02d}".format(*t_2))
# Task 5
l_1 = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {l_1[0][:-1]} is {l_1[1]} and \
the weight of a {l_1[2][:-1]} is {l_1[3]}")
print(f"The weight of an {l_1[0][:-1].upper()} is {l_1[1]*1.2:.1f} and \
the weight of a {l_1[2][:-1].upper()} is {l_1[3]*1.2:.1f}")
# Task 6
inventory = [
    ['Cabarnet', 10, 109.99],
    ['Pinot Noir', 4, 100],
    ['Chardonnay', 2, 49.5],
    ['Port', 125, 7000],
    ['Shiraz', 6, 45.45],
]
row = "{wine:<15s} {age:3d} {price:10.2f}".format
for i in inventory:
    print(row(wine=i[0], age=i[1], price=i[2]))
t_3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"{''.join(str(x).rjust(5, ' ') for x in t_3)}")
#  f'unpack a list: {" ".join(str(x) for x in a)}'