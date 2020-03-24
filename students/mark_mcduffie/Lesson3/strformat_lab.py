'''
Mark McDuffie
String Formatting
Lesson 3
'''

tuple1 = (2, 123.4567, 10000, 12345.67)
tuple2 = (1,2,3)
tuple3 = (4, 30, 2017, 2, 27)
list1 = ['oranges', 1.3, 'lemons', 1.1]

#Task one
#reformat tuple 1
def task1(tuple1):
    format = 'file_{:0>3d} :{:8.2f}, {:.2e}, {:.3g}'.format(*tuple1)
    return format

#reformat tuple1 to look the same as task one but use a different method
def task2(tuple1):
    a = '%03d' % (tuple1[0])
    b = '% 8.2f' % (tuple1[1])
    c = '%.2e' % (tuple1[2])
    d = '%.3g' % (tuple1[3])
    format = 'file_{} :{}, {}, {}'.format(a, b, c, d)
    return format

# Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)"
def task3(tuple2):
    form_string = "the 3 numbers are: {:d}, {:d}, {:d}"
    return form_string.format(*tuple2)

#given a 5 element tuple, use string formatting to print everything 2 digits,
#in different positions ( 4, 30, 2017, 2, 27) --> '02 27 2017 04 30'
def task4(tuple3):
    format = '{3:0>2d}, {4:d}, {2:d}, {0:0>2d}, {1:d}'.format(*tuple3)
    new = ''.join(format.split(','))
    return new

#given a 4 element list, write an f string that will display a sentence
def task5(list1):
    orange = list1[0]
    oWeight = list1[1]
    lemon = list1[2]
    lWeight = list1[3]
    format = f'the weight of an {orange[:-1]} is {oWeight} and the weight of a {lemon[:-1]} is {lWeight}'
    format2 = f'the weight of an {orange[:-1].upper()} is {1.2*oWeight} and the weight of a {lemon[:-1].upper()} is {1.2*lWeight}'
    return format, format2

def task6():
    """Write some Python code to print a table of several rows, each with a name, an age and a cost.
    Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
        """
    #x = '{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')
    list = [['Jim', 41, 20000],
         ['Mike', 35, 10000],
         ['Joe', 24, 100],
         ['Bob', 25, 900]]
    #loops for every row, giving each attribute 7 total spaces
    for row in list:
        print('{:>{width}s} {:>{width}d} {:>{width}d}'.format(*row, width=7))

#call all functions
print(task1(tuple1))
print(task2(tuple1))
print(task3(tuple2))
print(task4(tuple3))
print(task5(list1))
print(task6())