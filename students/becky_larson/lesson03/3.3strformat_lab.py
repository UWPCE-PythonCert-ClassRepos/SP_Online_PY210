# !/usr/bin/env python3
"""
Completed 8/23/2020 but realized 10/17/202 it hadn't been turned in for grade.
Added the extra assignment.
10/17/2020: update git and turn in
"""


def task1(input):
    print(f"\n++++++++++ {task1.__name__} ++++++++++\n")
    # First element is used to generate filename to help with sorting
    the_list = list(input)

    # pad filename numbers with zeros to get the right sort order.
    file_name = str(input[0]). zfill(3)
    # floating number in. Display 2 decimal places
    field1 = str(round(input[1], 2))
    #  integer in. Display scientific notation, 2 decimal places.
    field2 = "{:.2e}".format(input[2])
    # float in. Display scientific notation with 3 significant
    field3 = "{:.2e}".format(input[3])

    txt = "file_{0} : {1}, {2}, {3}"
    formatted_string = txt.format(file_name, field1, field2, field3)
    return formatted_string


def task2(input):
    print(f"\n++++++++++ {task2.__name__} ++++++++++\n")
    # same input as task1 but use different formatting method
    the_list = list(input)

    file_name = str(input[0]). zfill(3)
    field1 = str(round(input[1], 2))
    field2 = "{:.2e}".format(input[2])
    field3 = "{:.2e}".format(input[3])

    return f"file_{file_name} : {field1}, {field2}, {field3}"


def formatter_task3(*in_tuple):
    print(f"\n++++++++++ {formatter_task3.__name__} ++++++++++")
    print(f"\tHow many values passed? {len(in_tuple)}\n")

    ll = len(in_tuple)
    ll_2 = len(in_tuple)-1
    # dynamically build format string to accommodate length of tuple
    form_string = "the {} numbers: ".format(ll) + "{:d}, " * (ll_2) + "{:d}"
    formatted_string = ((form_string).format(*in_tuple))

    return formatted_string


def task4(ff):
    print(f"\n++++++++++ {task4.__name__} ++++++++++\n")
    print("task4: ", ff)
    # given a tuple, use index numbers to specify positions
    return f'{ff[3]:02d} {ff[4]:d} {ff[2]:d} {ff[0]:02d} {ff[1]:d}'
    # "{:02d} {:d} {:d} {:02d} {:d}".format(ff[3], ff[4], ff[2], ff[0], ff[1])


def task5(input):
    print(f"\n++++++++++ {task5.__name__} ++++++++++\n")
    print("task5: ", input)
    f1 = input[0]
    f2 = input[2]
    f3 = input[3]
    txt = "he weight of"
    return f'T{txt} an {f1[:-1]} is {input[1]} and t{txt} a {f2[:-1]} is {f3}'


def task6(input):
    print(f"\n++++++++++ {task6.__name__} ++++++++++\n")
    print("task6: ", input)
    # print table of several rows, with name, age and cost
    # Make some costs in hundreds and thousands to test alignment specifiers.
    len_list = [max(len(str(x)) for x in line) for line in zip(*arr)]
    print(len_list)
    name_len = len_list[0] + 3
    age_len = len_list[0] + 4
    cost_len = str(len_list[0] + 3) + "," + ".2f"
    print(name_len)

    for row in input:
        print(f'{row[0]:{name_len}}{row[1]:{age_len}}{row[2]:{cost_len}}')


def task6_extra(input):
    print(f"\n++++++++++ {task6_extra.__name__} ++++++++++\n")
    print("task6_extra: ", input)

    for row in input: 
        print("{:5}".format(row), end=" ")


# This it to be contents in tuple '02 27 2017 04 30'
in_tuple = (2, 123.4567, 10000, 12345.67)
output1 = task1(in_tuple)
print((output1))

output2 = task2(in_tuple)
print((output2))

print(formatter_task3(2, 3, 5))
print(formatter_task3(2, 3, 5, 7, 9))

task4_input = (4, 30, 2017, 2, 27)
print(task4(task4_input))

print(task5(['oranges', 1.3, 'lemons', 1.1]))

arr = [['Elizabeth', 37, 106310.23], ['Ann', 14, 1023.01], ['Jackson', 52, 30]]
# max length of each column
# print([max(len(str(x)) for x in line) for line in zip(*arr)])
task6(arr)
task6_extra(range(10))
