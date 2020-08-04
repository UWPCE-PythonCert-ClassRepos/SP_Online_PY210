#! python

#------------------------------------------------
# Lesson 3 - Exercise 3.3: String Formatting lab
#------------------------------------------------

# Task One
# Write a format string that will take the following four element tuple
# and produce this result 'file_002 :   123.46, 1.00e+04, 1.23e+04'
numbers = ( 2, 123.4567, 10000, 12345.67)
print("file_{:03d} :{:9.2f}, {:.2e}, {:.2e}".format(*numbers))


# Task Two
# Repeat Task 1 with alternate type of String
print(f"file_{numbers[0]:03d} :{numbers[1]:9.2f}, {numbers[2]:.2e}, {numbers[3]:.2e}")


# Task Thress
#Rewrite:
#    "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
#    to take an arbitrary number of values and put the code into a function

def formatter(in_tuple):
    placeholders = "{:d}"
    placeholders *= len(in_tuple)
    format_string = "the {:d} numbers are: " + '}, {'.join(placeholders.split('}{'))
    return format_string.format(len(in_tuple), *in_tuple)

# run some tests
print(formatter((16, 30, 5, 7, 18)))
print(formatter((2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30)))


# Task Four
#Given a 5 element tuple:
#    use string formating to print:
#    '02 27 2017 04 30'
numbers = (4, 30, 2017, 2, 27)
print("{:02d} {:d} {} {:02d} {:d}".format(*numbers[3:], numbers[2], *numbers[:2]))


# Task Five
# Given the following four element list:
#     Write an f-string that will display:
#     The weight of an orange is 1.3 and the weight of a lemon is 1.1
fruits = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {fruits[0][:-1]} is {fruits[1]} and the weight of a {fruits[2][:-1]} is {fruits[3]}")

#Now display the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
print(f"The weight of an {fruits[0][:-1].upper()} is {fruits[1]*1.2} and the weight of a {fruits[2][:-1].upper()} is {fruits[3]*1.2}")


#Task Six
#Write some Python code to print a table of several rows, each with a name, an age and a cost.
#Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
data = (
    ( 'Peter Wilson', 17, 1125.75 ),
    ( 'John Smith', 9, 572.34),
    ( 'Stephanie Gaines', 51, 46305.25),
    ( 'Joanne Walker', 58, 133829.60),
    ( 'Sam Hayes', 6, 76750842.99),
    ( 'Jimmy Brown', 23, 875.98),
    ( 'Diane Johnson',45, 854390223.78),
)

row = "| {name:<20s} | {age:2d} | {cost:13.2f} |".format

for col in data:
    print(row(name=col[0], age=col[1], cost=col[2]))

#For an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly
#print the tuple in columns that are 5 charaters wide? It can be done on one short line!
numbers = (9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
print(f"{'{:5d}'*10}".format(*numbers))
