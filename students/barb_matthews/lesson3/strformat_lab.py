#! /usr/bin/env python3

## Exercise 3.3 String Formatting
## By: B. Matthews
## 9/22/20

stuff = (2, 123.4567, 10000, 12345.67)
l = len(stuff)
test_tuple = (8, 4, 5, 11, 222, 9, 1)


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

do_this()
do_another_thing()
print("The test results = ")
formatter(test_tuple)

