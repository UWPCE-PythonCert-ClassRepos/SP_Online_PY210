#!/usr/bin/env python3


task_one_and_two_tuple = (2, 123.4567, 10000, 12345.67)


def task_one(x=task_one_and_two_tuple):
    '''Returns a format string using older string formatter'''
    return "file_%03d :   %.2f, %.2e, %.3e" % x


def task_two(x=task_one_and_two_tuple):
    '''Returns a form string using newer format method'''
    return "file_{:0>3d} :   {:.2f}, {:.2e}, {:.3e}".format(*x)


task_three_tuple = (3, 234, 66, 222, 77, 4, 24545, 34, 311, 1, 0, 2)


def task_three(x=task_three_tuple):
    '''Returns each value of a passed tuple in a formatted string'''
    form_string = f"The {len(x)} numbers are"
    for _ in x:
        form_string = form_string + "{:d}, "
    return form_string.format(*x)


task_four_tuple = (4, 30, 2017, 2, 27)


def task_four(x=task_four_tuple):
    '''Returns tuple values using their index as reference'''
    return "{3:0>2d}, {4:0>2d}, {2:0>2d}, {0:0>2d}, {1:0>2d}".format(*x)


task_five_list = ['oranges', 1.3, 'lemons', 1.1]


def task_five(x=task_five_list):
    '''Returns an fstring formatted list'''
    return "The weight of an " \
        f"{x[0]:.6} is {x[1]} and the weight of a {x[2]:.5} is {x[3]}"


def task_five_point_five(x=task_five_list):
    '''Returns an fstring formatted list with additional expressions applied'''
    return "The weight of an " \
        f"{x[0].upper():.6} is {x[1]*1.2} "\
        f"and the weight of a {x[2].upper():.5} is {x[3]*1.2}"


task_six_list = [["Bowie", 2.5, "$250"],
                 ["Brody", 8, "$1,201"],
                 ["Bodie", 4, "$17"],
                 ["Bugsey", 19, "$293,000"]]


def task_six(x=task_six_list):
    '''Prints list objects in a grid pattern using string formatting methods'''
    print("| {:^10} | {:^10} | {:^10} |".format('Name', 'Age', 'Cost'))
    for i in range(len(x)):
        print(f"| {x[i][0]:^10} | {x[i][1]:^10} | {x[i][2]:^10} |")
    return


task_six_point_five_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def task_six_point_five(x=task_six_point_five_tuple):
    '''Prints a single line of 10 tuple values, formatted'''
    print("{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}".format(*x))
    return
