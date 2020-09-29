#!/usr/bin/env python3

# Task 1
tuple = (2, 123.4567, 10000, 12345.67)
print("file_{:0>3} : {:.2f}, {:.2e}, {:.2e}".format(*tuple))

# Task 2
print(f"file_{tuple[0]:0>3} : {tuple[1]:.2f}, {tuple[2]:.2e}, {tuple[3]:.2e}")

# Task 3
def formatter(in_tuple):
    format_list = []
    for i in range(len(in_tuple)):
        format_list.append("{:d}")
        format_list.append(", ")
    format_list.pop()

    form_string = "the " + str(len(in_tuple)) + " numbers are: " + "".join(format_list)
    return(form_string.format(*in_tuple))


print(formatter((1, 2, 3)))

# Task 4
tuple = (4, 30, 2017, 2, 27)
print("{3:0>2d} {4} {2} {0:02d} {1}".format(*tuple))

# Task 5
list = ['oranges', 1.3, 'lemons', 1.1]

print(f"The weight of an {list[0][:-1]} is {list[1]} and " \
      f"the weight of an {list[2][:-1]} is {list[3]}")

print(f"The weight of an {list[0][:-1].upper()} is {list[1]*1.2} and " \
      f"the weight of an {list[2][:-1].upper()} is {list[3]*1.2}")

# Task 6
table = [['Ben', 25, '$765.44'],
         ['Dave', 56, '$2090.23'],
         ['Mike', 39, '$1570.06']]

for row in table:
    print("{:<10}{:>5d}{:>15}".format(*row))

# Extra Task
tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(str("{:5}\n"*len(tuple)).format(*tuple))
