#! /usr/bin/env python3

## Exercise 3.3 String Formatting
## By: B. Matthews
## 9/22/20

stuff = (2, 123.4567, 10000, 12345.67)
l = len(stuff)
test_tuple = (8, 4, 5, 11, 222, 9, 1)
tt = (4, 30, 2017, 2, 27)
list_of_stuff = ['oranges', 1.3, 'lemons', 1.1]
table_data = ("Bilbo", 111, 1000.11), ("Gandalf", 150, 50.12), ("Sue", 22, 2.15)

## Task 1
def do_this():
    print("file_{0:0>3d} : {1:.2f}, {2:.2e}, {3:.2e}".format(*stuff))

## Task 2
def do_another_thing():
    print(f"file_{stuff[0]:0>3d} : {stuff[1]:.2f}, {stuff[2]:.2e}, {stuff[3]:.2e}")

## Task 3
def formatter(in_tuple):
    how_long = len(in_tuple)
    a = ", ".join(["{}"]*how_long)
    print("length: ", how_long, "tuple: ", a.format(*in_tuple))
    return a.format(*in_tuple)

## Task 4
def something(in_tuple):
    a, b = "{:02d}".format(in_tuple[3]), "{:02d}".format(in_tuple[0])
    print(f"{a} {in_tuple[4]} {in_tuple[2]} {b} {in_tuple[1]}")

## Task 5
def task5(list_one):
    print(f"The weight of an {list_one[0][:-1]} is {list_one[1]} and the weight of a "
          f"{list_one[2][:-1]} is {list_one[3]}")
    print(f"The weight of an {list_one[0][:-1].upper()} is {list_one[1] * 1.2} and the weight of a "
          f"{list_one[2][:-1].upper()} is {list_one[3] * 1.2}")

## Task 6
def task6(data):
    for i in data:
        print("{0:<12} {1:>5} {2:>12}".format(*i))

do_this()
do_another_thing()
print("The test results = ")
formatter(test_tuple)
something(tt)
task5(list_of_stuff)
task6(table_data)

