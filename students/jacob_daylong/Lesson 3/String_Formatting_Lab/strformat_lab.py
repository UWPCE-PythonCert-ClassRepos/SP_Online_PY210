
#Task 1
# take is ( 2, 123.4567, 10000, 12345.67)
# turn into this 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print("Task 1:")
format_this = ( 2, 123.4567, 10000, 12345.67)
print("file_{0:0>3d} : {1:.2f}, {2:.2e}, {3:.2e}".format(*format_this))
print()


#Task 2
#Using your results from Task One, repeat the exercise, 
#but this time using an alternate type of format string 
#(hint: think about alternative ways to use .format() 
#(keywords anyone?), and also consider f-strings if 
#you’ve not used them already).
print("Task 2:")
print(f"file_{format_this[0]:0>3d} : {format_this[1]:.2f}, {format_this[2]:.2e}, {format_this[3]:.2e}")
print()

#Task 3
print("Task 3:")
def formatter(in_tuple):
    str_format = str('{:d}, ' * len(in_tuple[:-1]) + str(f'{in_tuple[-1]:d}'))
    return str_format.format(*in_tuple)

in_tuple = (1, 2, 3, 4)
tuple_len = len(in_tuple)

print("the " + str(tuple_len) + " numbers are: " + formatter(in_tuple))
print()

#Task 4
#Given a 5 element tuple:
#( 4, 30, 2017, 2, 27)
#use string formating to print:
#'02 27 2017 04 30'
print("Task 4:")
format_this = ( 4, 30, 2017, 2, 27)
print("{3:0>2d} {4} {2} {0:0>2d} {1}".format(*format_this))
print()

#Task 5
#Here’s a task for you: Given the following four element list:
#['oranges', 1.3, 'lemons', 1.1]
#Write an f-string that will display:
#The weight of an orange is 1.3 and the weight of a lemon is 1.1
#Now see if you can change the f-string so that it displays the 
#names of the fruit in upper case, and the weight 20% higher 
#(that is 1.2 times higher).
print("Task 5a:")
format_this = ('orange', 1.3, 'lemon', 1.1)
print(f"The weight of an {format_this[0]} is {format_this[1]} and the weight of a {format_this[2]} is {format_this[3]}.")
print()
print("Task 5b:")
print(f"The weight of an {format_this[0]} is {format_this[1]*1.2} and the weight of a {format_this[2]} is {format_this[3]*1.2}.")

#Task 6
