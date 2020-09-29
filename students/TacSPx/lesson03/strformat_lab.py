# ---------------------------------------------------------------------------- #
# Title: strformat_lab
# Description: string format lab
#   6 Tasks to complete
# ---------------------------------------------------------------------------- #

# Task 1
# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'


task1_tuple = "file_00{}, {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67)
print("Task 1 =", task1_tuple)

# Task 2
# Using your results from Task One, repeat the exercise, but this time using an alternate type of format string
# (hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve
# not used them already).

task2_tuple = (2, 123.4567, 10000, 12345.67)

f_str = f"file_00{task2_tuple[0]:1}, {task2_tuple[1]:.2f}, {task2_tuple[2]:.2e}, {task2_tuple[3]:.2e}"
print("Task 2 =", f_str)

# Task 3
# Dynamically Building up format strings
# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# Have python count how many item you have and display them back

seq = (4,5,6,7,8)
def formatter(seq):
    lgth = len(seq)
    return "There are {} items, and they are: ".format(lgth) + ", ".join(["{}"] * lgth).format(*seq)
print("Task 3 =",formatter(seq))

# Task 4
# Given a 5 element tuple:
# ( 4, 30, 2017, 2, 27)
# use string formating to print:
# '02 27 2017 04 30'
# (3) (4) (2) (0) (1)
# Hint: use index numbers to specify positions.
# used ":0>2d" to add leading "0"
t4 = (4, 30, 2017, 2, 27)
t4_order = f"{t4[3]:0>2d}, {t4[4]}, {t4[2]}, {t4[0]:0>2d}, {t4[1]}"
print("Task 4 =", t4_order)


# Task 5
# 5 Part 1
# Given the following four element list:
# ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1

# 5 Part 2
# Now see if you can change the f-string so that it displays the names
# of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).

fruit = {"fruit1": "orange", "fruit2": "lemon"}
weight = {"weight1": 1.3, "weight2": 1.1}
task5 = f"The weight of an {fruit['fruit1']} is {weight['weight1']} and the weight of a {fruit['fruit2']} is {weight['weight2']}"
print("Task 5 =", task5)
task5_upper = f"The weight of an {fruit['fruit1'].upper()} is {weight['weight1']*1.2} and the weight of a {fruit['fruit2'].upper()} is {weight['weight2']*1.2}"
print("Task 5 upper =", task5_upper)


# Task 6
# Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are
# in the hundreds and thousands to test your alignment specifiers. And for an extra task, given a tuple with 10 consecutive numbers,
# can you work how to quickly print the tuple in columns that are 5 characters wide? It can be done on one short line!

# title
title = "******  Automotive Inventory  ******"
heading_name = ("| Name:", "| Age:", "| Cost:        |")
header = f"{heading_name[0].upper():<14s} {heading_name[1].upper():<1s} {heading_name[2].upper():<12s}"
print("Task 6 =")
print(title)
print(header)


# data
cars = [
    ["Toycar", 1, "$30"],
    ["Spectra", 17, "$995"],
    ["Challenger", 2, "$71,000"],
    ["Mustang", 53, "$250,000"],
    ["Ferrari", 5, "$3,500,000"],
]
# define format row
row = "| {Name:<12s} | {Age:4d} | {Cost:<12s} |".format

for car in cars:
    print(row(Name=car[0], Age=car[1], Cost=car[2]))

# for an extra credit task, given a tuple with 10 consecutive numbers,
# can you work how to quickly print the tuple in columns that
# are 5 characters wide? It can be done on one short line!

print("\nTask 6 extra =")
for columns in range(1,11):
    print(f"|{columns:<5d}", end="")
