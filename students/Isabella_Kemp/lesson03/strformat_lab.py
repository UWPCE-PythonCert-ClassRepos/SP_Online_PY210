# Isabella Kemp
# String Formatting Exercise
# 1/24/2020

# Task 1
# Write a format string that takes the following tuple.
tuple1 = (2, 123.4567, 10000, 12345.67)
print("file_{:03}, {:.2f}, {:.2e}, {:.2e}".format(*tuple1))

# Task 2
# A different way to format string
print("Task 2 formatting")
format_task2 = f"file_{tuple1[0]:03}, {tuple1[1]:.2f}, {tuple1[2]:.2e}, {tuple1[3]:.2e}"
print(format_task2)

# Task 3
# Dynamically building format strings
def formatter(in_tuple):
    l = len(in_tuple)
    string = ("The {} numbers are: " + ', '.join(['{:d}'] * l)).format(l, *in_tuple)
    return string
tuple1 = (3, 6, 7)
tuple2 = (8, 4, 7, 9, 3, 5)
print(formatter(tuple1))
print(formatter(tuple2))

# Task 4
# Uses index numbers to specify positions.
new_tuple = (4, 30, 2017, 2, 27)
print(f"{new_tuple[3]:02d} {new_tuple[4]} {new_tuple[2]} {new_tuple[0]:02d} {new_tuple[1]}")

# Task 5
elements = ('orange', 1.3, 'lemon', 1.1)
print(f"The weight of an {elements[0].upper()} is {elements[1]*1.2} and the weight of a {elements[2].upper()} is {elements[3]*1.2}")

# Task 6
# Write python code to print a table of several rows, each with a name, an age
# and a cost.
str_task6 = (("Joe", 35, "$3000"), ("Diana", 40, "$6000"), ("Robert", 20, "$1000"), ("Olivia", 15, "$3500"))
def table(str_task6):
    print("| {:^10} | {:^10} | {:^10} |".format('Name', 'Age', 'Cost'))
    print("-"*40)
    for i in range(len(str_task6)):
        print(f"| {str_task6[i][0]:^10} | {str_task6[i][1]:^10} | {str_task6[i][2]:^10} |")
    return

table(str_task6)

# extra task
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
l = ' '.join(list(['{:^5d}']*10)) # gives us 5 characters wide
print(l.format(*t))
