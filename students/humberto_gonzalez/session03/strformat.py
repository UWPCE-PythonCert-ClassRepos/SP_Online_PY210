#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:24:50 2019

@author: humberto gonzalez
"""


# Task 1

tuple_1 = (2, 123.4567, 10000, 12345.67)
formatter_t1 = 'file_{0:03d} : {1:10.2f}, {2:.2e}, {3:.2e}'
print(formatter_t1.format(*tuple_1))


# Task 2
tuple_2 = (2, 123.4567, 10000, 12345.67)
formatter_t2 = f'file_00{tuple_2[0]} : {round(tuple_2[1],2)}, {tuple_2[2]}, {tuple_2[3]}'
print(formatter_t2)


# Task 3

def formatter(seq):
    '''Takes in a tuple and formats the values into a string'''
    n = len(seq)
    string = 'the {} numbers are: '.format(n) + ', '.join(['{}']*n)
    return string.format(*seq)


# Task 4

tuple_4 = (4, 30, 2017, 2, 27)    
formatter_t4 = '{3:02d} {4:} {2:} {0:02d} {1:}'
print(formatter_t4.format(*tuple_4))


# Task 5

list_5 = ['oranges', 1.3, 'lemons', 1.1]

fruit_a = list_5[0]
weight_a = list_5[1]
fruit_b = list_5[2]
weight_b = list_5[3]


print(f'The weight of an {fruit_a[:-1]} is {weight_a} and the weight of a {fruit_b[:-1]} is {weight_b}')
print(f'The weight of an {fruit_a[:-1].upper()} is {weight_a*1.2} and the weight of a {fruit_b[:-1].upper()} is {weight_b*1.2}')


### TESTING ###
if __name__ == "__main__":
    # run some tests on the above functions
    a_tuple = (2, 3, 5)
    b_tuple = (2, 3, 5, 7, 9)
    

    assert formatter(a_tuple) == 'the 3 numbers are: 2, 3, 5'
    assert formatter(b_tuple) == 'the 5 numbers are: 2, 3, 5, 7, 9'
    print("tests passed")