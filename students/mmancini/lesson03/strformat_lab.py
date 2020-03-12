#!/usr/bin/env python3


def formatter(tup):
    s = ""
    for i in tup:
        if s != "":
            s = s + ", "

        s = s + str(i)

    return s


def task1(tup):
    print("task 1 output without padding ==> " + 'file{:03d} : {:.2f}, {:.2E} , {:.2E}'.format(*tup))
    print("task 1 output with padding ==> " + 'file{:>03d} : {:.2f}, {:.2E} , {:.2E}'.format(*tup))


def task2(tup):
    print("task 2 output ==> " + 'file{:>03d} : {:.2f}, {:.2E} , {:.2E}'.format(*tup))
    print("task 2 output with f string ==> " + f'file00{tup[0],2} : {tup[1]:.2f}, {tup[2]:.2E}, {tup[3]:.2E}')


def task3(tup):
    s = formatter(tup)
    print("task 3 output, the numbers are ==> " + s)


def task4(tup):
    print("task 4 output ==> " + '0{:d} {:d} {:d} 0{:d} {:d}'.format(tup[3], tup[4], tup[2], tup[0], tup[1]))


def task5(tup):
    s = f'The weight of an {tup[0].upper()} is {tup[1] * 1.2} and the weight of a {tup[2].upper()} is {tup[3] * 1.2}'
    print("task 5 output ==> " + s)


def task6():
    table_data = [
        ['Joe', 21, 11.22],
        ['Sally', 23, 7.8],
        ['Betty', 9, 123.456]
        ]
    for row in table_data:
        print("{: >20} {: >20} {: >20}".format(*row))


####################################


# main, test funcs

if __name__ == "__main__":
    # run some tests
    xTup = (2, 123.4567, 10000, 12345.67)
    xTup3 = (1, 2, 3, 4, 5)
    xTup4 = (4, 30, 2017, 2, 27)
    xTup5 = ['oranges', 1.3, 'lemons', 1.1]

    task1(xTup)
    task2(xTup)
    task3(xTup3)
    task4(xTup4)
    task5(xTup5)
    task6()
