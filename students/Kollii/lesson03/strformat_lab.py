
# Task One
"""a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""
print("## Task One ##\n")
string = (2, 123.4567, 10000, 12345.67)
print("A string: ", string)

formated_str = "file_{:03d} : {:10.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67)
print("Fromated string: ", formated_str)


# Task Two
print("\n## Task Two ##\n")
#alternative method to achieve task one

print("alternate type of format string\n")
print(f"file_{string[0]:0>3d} :   {string[1]:.2f}, {string[2]:.2e}, {string[3]:.3e}")

# Task Three

print("\n## Task Three ##\n")
print("Dynamically Building up format strings\n")
def formatter(in_tuple):
    count = len(in_tuple)
    str_output = ('the {} numbers are: ' +
    ', '.join(['{:d}'] * count)).format(count,*in_tuple)
    return str_output

tuple1= (2,3,5)
tuple2 = (2,3,5,7,9)

print(formatter(tuple1))

print(formatter(tuple2 ))

# Task Four
print("\n## Task Four ##\n")

# given a 5 element tuple ( 4, 30, 2017, 2, 27)
# use string formating to print: '02 27 2017 04 30'

tuple4 = (4, 30, 2017, 2, 27)
print("{3:0>2d} {4:0} {2:0} {0:0>2d} {1:0}".format(*tuple4))


# Task Five
print("\n## Task Five ##\n")

# Here’s a task : Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display: The weight of an orange is 1.3 and the weight of a lemon is 1.1

list1 = ['oranges', 1.3, 'lemons', 1.1]

print("f-string:  ", f'The weight of an {list1[0][:-1]} is {list1[1]} and the weight of a {list1[2][:-1]} is {list1[3]}')

print("change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher)")

print(f'The weight of an {list1[0].upper()[:-1]} is {list1[1] * 1.2} '
      f'and the weight of a {list1[2].upper()[:-1]} is {list1[3] * 1.2}')


# Task Six
print("\n## Task Six ##\n")

print(" print a table of several rows, each with a name, an age and a cost ")
tuple6 = list()
tuple6.append(("Abc", 25, 12345))
tuple6.append(("Xyzh", 35, 4567))
tuple6.append(("Pqrst", 45, 6789))
tuple6.append(("Mnopsdf", 15, 2345))

for t in tuple6:
     print('{:10}{:5}{:15.{d}f}'.format(*t, d=2))

#extra task: given a tuple with 10 consecutive numbers, print tuple in columns that are 5 char wide
tuple_extra = (1,2,3,4,5,6,7,8,9,10)

print("given a tuple with 10 consecutive numbers, print tuple in columns that are 5 char wide")
print(('{:{wide}}'*10).format(*tuple_extra, wide=5))    

