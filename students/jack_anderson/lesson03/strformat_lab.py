#!/usr/bin/env python3


"""
Task One
Write a format string that will take the following four element tuple: ( 2, 123.4567, 10000, 12345.67)
and produce: 'file_002 :   123.46, 1.00e+04, 1.23e+04'

Task Two
Using your results from Task One, repeat the exercise, but this time using an alternate type of format string
(Hint: Think about alternative ways to use '.format(), and also consider f-strings if you've not used them already

Task Three
Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)" to take an arbitrary number of values

Task Four
Given a 5 element tuple of ( 4, 30, 2017, 2, 27), use string formatting to print '02 27 2017 04 30'

Task Five
Given the following four elemental list ['oranges', 1.3, 'lemons', 1.1] , write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1
Then, change the f-string so that it displays the names of the fruit in upper case,
and the weight 20% higher (that is 1.2 times higher).

Task Six
Write some Python code to print a table of several rows, each with a name, an age and a cost.
Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
For an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple
in columns that are 5 charaters wide? It can be done on one short line!
"""

turp = ( 2, 123.4567, 10000, 12345.67)
turp2 = ( 1, 2, 3, 4, 5, 6, 7)
turp3 = ( 4, 30, 2017, 2, 27)
t3_result = '02 27 2017 04 30'
turp_result = 'file_002 :   123.46, 1.00e+04, 1.23e+04'
list_5 = ['oranges', 1.3, 'lemons', 1.1]


# Task One
def task_one(x):
    converted = f"file_{(x[0]):03d} :{(x[1]):9.2f}, {(x[2]):2.2e}, {(x[3]):2.2e}"
    return(converted)


# Task Two
def task_two(x):
    fname = 'file_{:03d} :'.format(x[0])
    float_num1 = '{:9.2f},'.format(x[1])
    int_num1 = ' {:2.2e},'.format(x[2])
    float_num2 = ' {:2.2e}'.format(x[3])

    return(fname + float_num1 + int_num1 + float_num2)


def task_three(x):
    count = len(x)

    if count > 1:
        a = "{:d}, " * (count - 1) + "{:d}"
    else:
        a = "{:d}"

    z = f"the {count} numbers are: "
    form_string = z + a

    return(form_string.format(*x))



def task_four(x):
    month = x[3]
    day = x[4]
    year = x[2]
    hour = x[0]
    min = x[1]

    string_formatting = "{:02d} {:2d} {:4d} {:02d} {:2d}".format(month, day, year, hour, min)

    print(string_formatting)



def task_five(x):
    orange = (x[0])[:-1]
    lemon = (x[2])[:-1]
    o_weight = x[1]
    l_weight = x[3]
    print(f"The weight of an {orange.upper()} is {o_weight * 1.2} "
          f"and the weight of a {lemon.upper()} is {l_weight * 1.2}")





def test(x):
    return(task_five(x))


test(list_5)