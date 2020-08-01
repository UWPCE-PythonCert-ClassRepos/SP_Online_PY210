#!/usr/bin/env python3

# Dominic Divakaruni
# SP_Online_PY210
# Lesson 02 - Grid Printer Exercise

import math 
# part 1 and 2
def print_grid(x=8, y=2):
    for n in range (y):
        print("+ ","- "* math.floor(x/2),"+ ","- "* math.floor(x/2),"+")
        for n in range (math.floor(x/2)):
            print("| ","  "* math.floor(x/2),"| ","  "* math.floor(x/2),"|")
    print("+ ","- "* math.floor(x/2),"+ ","- "* math.floor(x/2),"+")

# part 3
def print_grid2(x=5, y=2):
    if x>0:
        print("+ ", end = " ")
        for i in range (x):
            print("- "*y, "+ ", end = " ")
        print(" ")
        for j in range (x):
            for k in range (y):
                for l in range (x+1):
                    print("| ", "  "*y, end = " ")
                print(" ")
            print("+ ", end=" ")
            for m in range (x):
                print("- "*y, "+ ", end = " ")
            print(" ")
            