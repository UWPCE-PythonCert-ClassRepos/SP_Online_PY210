#!/usr/bin/env python3


def task1(input_tuple):
    formatted_string = "file_{:0>3d} :   {:.2f}, {:.2e}, {:.3g}".format(*input_tuple)
    print(formatted_string)


def task2(seq):
    formatted_string = f"file_{seq[0]:0>3d} :   {seq[1]:.2f}, {seq[2]:.2e}, {seq[3]:.3g}"
    print(formatted_string)


def task3(seq):
    number = len(seq)
    formatted_string = ("the {} numbers are: " + ", ".join(["{}"] * number)).format(number, *seq)
    print(formatted_string)


def task4(seq):
    formatted_string = f"{seq[3]:0>2d} {seq[4]} {seq[2]} {seq[0]:0>2d} {seq[1]}"
    print(formatted_string)


def task5(seq):
    formatted_string = f"The weight of an {seq[0][0:-1]} is {seq[1]} and the weight of a {seq[2][0:-1]} is {seq[3]}"
    print(formatted_string)
    next_string = (
        f"The weight of an {seq[0][0:-1].upper()} is {seq[1]*1.2} "
        f"and the weight of a {seq[2][0:-1].upper()} is {seq[3]*1.2}"
    )
    print(next_string)


def task6(table):
    width = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]
    for row in table:
        row_string = "{0:>{w1}}{1:>{w2}}{2:>{w3}}".format(*row, w1=width[0]+2, w2=width[1]+2, w3=width[2]+2)
        print(row_string)


def task6_bonus(seq):
    print(("{:5}"*10).format(*seq))


if __name__ == '__main__':
    start_tuple = (2, 123.4567, 10000, 12345.67)
    task1(start_tuple)
    task2(start_tuple)
    three_element_tuple = (1, 2, 3)
    task3(three_element_tuple)
    task4_tuple = (4, 30, 2017, 2, 27)
    task4(task4_tuple)
    task5_list = ['oranges', 1.3, 'lemons', 1.1]
    task5(task5_list)
    task6_table = [["Name", "Age", "Cost"], ["Chardonnay", 10, "$15,000"], ["Pinot noir", 5, "$20"]]
    task6(task6_table)
    task6_bonus_tuple = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    task6_bonus(task6_bonus_tuple)
