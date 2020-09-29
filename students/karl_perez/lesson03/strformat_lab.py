#Procedure
#Create a new file called strformat_lab.py in your student dir in the class repo.
#When the empty script is available and runnable, complete the following four tasks.

"""Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce
'file_002 :   123.46, 1.00e+04, 1.23e+04"""

#Task1
a_string = ( 2, 123.4567, 10000, 12345.67)
new_string = 'file_{:03d} :  {:6.2f}, {:.2e}, {:.2e}'.format(2, 123.4567, 10000, 12345.67)
print(new_string) 

# Task 2
"""Using your results from Task One, repeat the exercise, but this time using an alternate type of format string (hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve not used them already)."""

new_string_2 = f'file_{a_string[0]:03d} :  {a_string[1]:6.2f}, {a_string[2]:.2e}, {a_string[3]:.2e}'
print(new_string_2)

# Task 3 
"""Dynamically Building up format strings
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

to take an arbitrary number of values."""

def formatter(in_tuple):
    #tuplelength = len(in_tuple)
    #print(tuplelength)
    form_string = str('{:d},'*len(in_tuple))[:-1]
    #print(form_string)
    return form_string.format(*in_tuple)

# Task 4
"""Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'"""

tuplefour = (4, 30, 2017, 2, 27)
new_tuple = (f"{tuplefour[3]:0>2d} {tuplefour[4]:.0f} {tuplefour[2]:.0f} {tuplefour[0]:0>2d} {tuplefour[1]:0>2d}")
print(new_tuple)

# Task 5
"""Here’s a task for you: Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1"""

task5 = ['oranges', 1.3, 'lemons', 1.1]
task5_tuple = f"The weight of an {task5[0][0:-1]} is {task5[1]} and the weight of a {task5[2][0:-1]} is {task5[3]}"
print(task5_tuple)

#Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).

new_task5_tuple = f"The weight of an {task5[0][0:-1].upper()} is {task5[1]*1.2} and the weight of a {task5[2][0:-1].upper()} is {task5[3]*1.2}"
print(new_task5_tuple)

# Task 6
"""Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers."""

name = ["Jimmy", "Eddie", "Tony"]
age = ["28", "360", "4567"]
cost = ["$1.00", "$10.00", "$100.00"]

print(f"{name[0]:5} {age[0]:5} {cost[0]:5}")
print(f"{name[1]:5} {age[1]:5} {cost[1]:5}")
print(f"{name[2]:5} {age[2]:5} {cost[2]:5}")
