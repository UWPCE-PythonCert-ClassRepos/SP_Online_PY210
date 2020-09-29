#!/usr/bin/env python
# PY210 Lesson 3
# Jonathan Vu
def formatTask1():
    input = (2, 123.4567, 10000, 12345.67);
    formatter = 'file_00{} : {:.2f}, {:.2e}, {:.3g}'
    print(formatter.format(*input))

def formatTask2():
    input = (2, 123.4567, 10000, 12345.67);
    formatter = 'file_00%d : %.2f, %.2e, %.2e'
    print(formatter % input)

def formatTask3(numsIn):
    l = len(numsIn);
    formatter = "The {} numbers are : ".format(l) + ', '.join(["{}"]*l).format(*numsIn)
    return formatter

def formatTask4():
    input = [4,30, 2017, 2, 27];
    print('0{:d} {:d} {:d} 0{:d} {:d}'.format(input[3], input[4], input[2], input[0], input[1]))

def formatTask5():
    input = ['oranges', 1.3, 'lemons', 1.1];
    formatter = f'The weight of an {input[0].upper()} is {input[1]*1.2} and the weight of a {input[2].upper()} is {input[3]*1.2}'
    return formatter

def formatTask6():
    names = ['Peter','Ann','Jon','Mike','Justin','David'];
    ages = [55, 53, 24, 22, 20, 17];
    prices = [400, 300, 250, 250, 220, 150];

    print('{:^5} {:^15} {:}'.format('Name', 'Age', 'Prices'))

    for names,ages,prices in zip(names, ages, prices):
        print(f"{names:<10} {ages:^6} ${prices:>6.2f}")