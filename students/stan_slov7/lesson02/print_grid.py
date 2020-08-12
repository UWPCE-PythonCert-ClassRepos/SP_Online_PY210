#!/usr/bin/env python3


#----------------------------Part 1----------------------------

def line():
    print("+",("- " *4), end="")
   
def space():
    print("|", (" " *8), end="")


def linerow():
    line()
    line()
    print("+")

def spacerow():
    space()
    space()
    print("|")
   

def printRow():
    linerow()
    spacerow()
    spacerow()
    spacerow()
    spacerow()
 

def printGrid1():
    printRow()
    printRow()
    linerow()
    
print("literal function printGrid1() creating 2x2 grid of size '9':\n")
printGrid1()
print()

#----------------------------Part 2----------------------------

def line2(n):
    print("+",("- " *((n-1)//2)), end="")
    #force integer division
   
def space2(n):
    print("|", (" " *(n-1)), end="")


def linerow2(n):
    line2(n)
    line2(n)
    print("+")

def spacerow2(n):
    space2(n)
    space2(n)
    print("|")


def printRow2(n):
    linerow2(n)
    for i in range((n-1)//2):
        spacerow2(n)
        #force integer division


def printGrid2(n):
    printRow2(n)
    printRow2(n)
    linerow2(n)

#test2 
#with various sizes where param: n is unit size of whole grid length/width
print("test using printGrid2(n) function creating same 2x2 grid as before but with grid size n.\n")

print("2x2 grid with grid size param n=15:")
printGrid2(15)
print()

print("2x2 grid with grid size param n=3:")
printGrid2(3)
print()

print("2x2 grid with grid size param n=9: (identical to literal grid created with printGrid1, grid size 9)")
printGrid2(9)
print()
