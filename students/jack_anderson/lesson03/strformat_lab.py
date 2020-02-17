#!/usr/bin/env python3

# Test Variables
turp1 = ( 2, 123.4567, 10000, 12345.67)
turp3 = ( 1, 2, 3, 4, 5, 6, 7)
turp4 = ( 4, 30, 2017, 2, 27)
list_5 = ['oranges', 1.3, 'lemons', 1.1]



# Task One
def task_one(x):
    """
    Action to take a 4 element tuple and format using f-string
    :param x: 4 element tuple
    :return: formats as 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """
    converted = f"file_{(x[0]):03d} :{(x[1]):9.2f}, {(x[2]):2.2e}, {(x[3]):2.2e}"
    return(converted)


# Task Two
def task_two(x):
    """
    Action to take a 4 element tuple and format using format()
    :param x: 4 element tuple
    :return: formats as 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """
    fname = 'file_{:03d} :'.format(x[0])
    float_num1 = '{:9.2f},'.format(x[1])
    int_num1 = ' {:2.2e},'.format(x[2])
    float_num2 = ' {:2.2e}'.format(x[3])

    return(fname + float_num1 + int_num1 + float_num2)


def task_three(x):
    """
    Action to take an arbitrary number of values and display the values as well as the total count of values
    :param x: Tuple or list containing n number of values
    :return: values and the total count of values passed
    """
    count = len(x)

    if count > 1:
        a = "{:d}, " * (count - 1) + "{:d}"
    else:
        a = "{:d}"

    z = f"the {count} numbers are: "
    form_string = z + a

    return(form_string.format(*x))



def task_four(x):
    """
    Action to take a 5 element tuple and format it to display in a date-time format
    :param x: tuple containing 5 elements
    :return: month / day / year / hour / minute
    """
    month = x[3]
    day = x[4]
    year = x[2]
    hour = x[0]
    min = x[1]

    string_formatting = "{:02d} {:2d} {:4d} {:02d} {:2d}".format(month, day, year, hour, min)

    print(string_formatting)



def task_five(x):
    """
    Action to format a 4 element list, print the 1 & 3 elements in Uppercase and multiply the 2 & 4th elements by 1.2
    :param x: List containing 4 elements
    :return: Message to user containing the name and weight of fruit in the provided list
    """
    orange = (x[0])[:-1]
    lemon = (x[2])[:-1]
    o_weight = x[1]
    l_weight = x[3]
    print(f"The weight of an {orange.upper()} is {o_weight * 1.2} "
          f"and the weight of a {lemon.upper()} is {l_weight * 1.2}")




def task_six():
    """
    Action to print a table of several rows, each with a name, an age and a cost. All items in rows are aligned
    :return: 4 rows with columns showing Name, Age, and Cost
    """
    x = ('NAME', 'AGE', 'COST')
    a = ('Jack', 42, '$100,000' )
    b = ('Stephanie', 9, '$1,200.97')
    c = ('Mr. Anderson', 100, '$900,000.99')
    z = '{name:{align}{width}}|{age:{align}{width}}|{cost:{align}{width}}|' \
          .format(name=x[0], age=x[1], cost=x[2], align='^', width='15')


    print('{name:{align}{width}}|{age:{align}{width}}|{cost:{align}{width}}|' \
          .format(name=x[0], age=x[1], cost=x[2], align='^', width='15'))
    print('{name:{align}{width}}|{age:{align}{width}}|{cost:{align}{width}}|'\
        .format(name=a[0], age=a[1], cost=a[2], align='^',width='15'))
    print('{name:{align}{width}}|{age:{align}{width}}|{cost:{align}{width}}|' \
        .format(name=b[0], age=b[1], cost=b[2], align='^', width='15'))
    print('{name:{align}{width}}|{age:{align}{width}}|{cost:{align}{width}}|' \
        .format(name=c[0], age=c[1], cost=c[2], align='^', width='15'))



######################################################################################
#   TESTING - uncomment the below code to run a test of the functions in this file   #
######################################################################################


# if __name__ == "__main__":
#     # Test tasks 1 - 5 and then run task 6
#     # Task One Test
#     assert task_one(turp1) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
#     print("Task 1 test passed")
#
#
#     # Task Two test
#     assert task_two(turp1) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
#     print("Task 2 test passed")
#
#
#     # Task Three test
#     assert task_three(turp3) == 'the 7 numbers are: 1, 2, 3, 4, 5, 6, 7'
#     print("Task 3 test passed")
#     print()
#
#
#     # Task Four test
#     print("Print task 4: ")
#     task_four(turp4)
#     print()
#
#     # Task Five Test
#     print("Print task 5: ")
#     task_five(list_5)
#     print()
#
#     # Task Six test
#     print("Print task 6: ")
#     task_six()
#     print()



