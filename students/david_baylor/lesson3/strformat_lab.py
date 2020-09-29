#!/usr/bin/env python3
from decimal import Decimal


"""
strformat_lab.py
By David Baylor on 10/29/19
uses python 3

"""

def formatter(in_tuple):
    form_string = "the {} numbers are: {}".format(len(in_tuple), "{}"+", {}"*(len(in_tuple)-1))

    return form_string.format(*in_tuple)

def tableMaker(row):
    print("{:10}{:4}{:8}".format(row[0], row[1], row[2]))
    

print("file_{} :   {}, {}, {}".format("2".zfill(3), round(123.4567, 2), '%.2E' % Decimal(10000), '%.2E' % Decimal(12345.67)))


file_name = "2"
example_float = 123.4567
int_scientific = 10000
float_scientific = 12345.67
print(f"file_{file_name.zfill(3)} :   {round(example_float, 2)}, {'%.2E' % Decimal(int_scientific)}, {'%.2E' % Decimal(float_scientific)}")

print(formatter((1,2,3,4,5)))

example_tuple = ( 4, 30, 2017, 2, 27)
print(f"{example_tuple[0]} {example_tuple[1]} {example_tuple[2]} {example_tuple[3]} {example_tuple[4]}")

example_list = ['orange', 1.3, 'lemon', 1.1]
print(f"The weight of an {example_list[0]} is {example_list[1]} and the weight of a {example_list[2]} is {example_list[3]}")

print("{:10}{:4}{:8}".format("name", "age", "cost"))
tableMaker(("Joe","24","$20.04"))
tableMaker(("Bill","56","$103.34"))
tableMaker(("Zach","15","$35.130"))
tableMaker(("john","30","$50.00"))
tableMaker(("luke","17","$-10.00"))
tableMaker(("Zach","102","$799.99"))

