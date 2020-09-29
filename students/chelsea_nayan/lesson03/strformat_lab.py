# chelsea_nayan, UWPCE, Python210
# Lesson 03: String Formatting Lab Exercise

# Task 1: --------------------------------------------
# Writes a format string that takes a four element tuple and produces a filename, a floating point number, an integer, and a float with a lot of digits

tuple_list = (2, 123.4567, 10000, 12345.67) # Result should be: "file_002: 123.46, 1.00e+0.4, 1.23+04"

def task1(ls): # I used literal string interpolation, AKA "f-strings"
    seq = list(ls)
    first, second, third = round(seq[1], 2), "{:.2e}".format(seq[2]), "{:.2e}".format(seq[3], 3)
    print(f"file_{(seq[0]//100)%10}{(seq[0]//10)%10}{(seq[0])%10}: {first}, {second}, {third}") # Readability it a bit hard here when trying to create the filname, but I initially didn't know there was a way to do fixed width formatting. I used integer division and modulo to grab the hundreds, tens, and ones place in the number and format each individually.

task1(tuple_list)

# Task 2: -----------------------------------------------
# The same as Task 1, just using a different type of format string

def task2(ls): # I used the format() method instead of f-strings
    seq = list(ls)
    first, second, third = round(seq[1], 2), "{:.2e}".format(seq[2]), "{:.2e}".format(seq[3], 3)
    print("file_{:03}: {}, {}, {}".format(seq[0], first, second, third)) # I used the more pythonic way of fixed number width formatting

task2(tuple_list)

# Task 3: ------------------------------------------------
# Rewrite -- "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) -- to take an arbitray number of values

nums = (37, 5)

def formatter(in_tuple):
    temp = '{:d}, ' * (len(in_tuple) - 1) + ('{:d}' if len(in_tuple) else '') # in case the tuple is empty (1 line if statements are weird to use..)
    form_string = "the {} numbers are: {}".format(len(nums), temp)
    return form_string.format(*in_tuple)

print(formatter(nums))

# Task 4: ------------------------------------------------
# Given a five element tuple, format it a specific way

five_tuple = (4, 30, 2017, 2, 27) # Supposed to print out "02 27 2017 04 30"

def formatter1(nums):
    arranged = "{:02} {} {} {:02} {}".format(nums[3], nums[4], nums[2], nums[0], nums[1])
    return print(arranged)

formatter1(five_tuple)

# Task 5: ------------------------------------------------
# Use f-strings. Given a four element list, display "The weight of an __ is __ and the weight of a __ is __. "

lst = ['oranges', 1.3, 'lemons', 1.1]
first_fruit, second_fruit = lst[0], lst[2] # Set the fruits in the list to their own variable
print(f"The weight of an {first_fruit[0:-1].upper()} is {lst[1] * 1.2} and the weight of a {second_fruit[0:-1].upper()} is {lst[3] * 1.2}") # Used f-string to display the fruits without their plural form and their weights

# Task 6: -------------------------------------------------
#  Print a table of several rows

names = ["Mickey", "Sora", "Riku", "Kairi", "Heartless"]
ages = ['1000000000000', '16', '18', '17', '10500000000000000000000000']
costs = ['$50,000.00', '$0.00', '$75,000,000,000,000.00', '$3.50', '$1,000.75']

# This function takes in 3 arguments that are each a list of strings. Prints out a dynamic column format.
def column_maker(name, age, cost):
    max_name, max_age, max_cost = len(max(name, key=len)), len(max(age, key=len)), len(max(cost, key=len))
    for i in range(len(name)): # Iterates through length of a list
        print(f"{name[i].ljust(max_name,' ')} {age[i].ljust(max_age,' ')} {cost[i].ljust(max_cost,' ')} ") #ljust left justifies an element. First argument is the number of times the second argument pads.
column_maker(names, ages, costs)
