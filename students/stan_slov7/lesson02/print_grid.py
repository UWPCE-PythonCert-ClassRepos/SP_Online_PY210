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

#----------------------------Part 3----------------------------

def line3(n,m):
    print("+",("- " *m), end="")
    
def space3(n,m):
    print("|", (" " *(2*m)), end="")


def linerow3(n,m):
    for i in range(n):
        line3(n,m)
    print("+")
    
def spacerow3(n,m):
    for i in range(n):
        space3(n,m)
    print("|")


def printRow3(n,m):
    linerow3(n,m)
    for i in range(m):
        spacerow3(n,m)
        
    
def printGrid3(n,m):
#where param: n is number of cells
#      param: m is grid cell width/length "unit" size 
    for i in range(n):
        printRow3(n,m)
    linerow3(n,m)
    

#test3
#where n number of rows/columns i.e. grids, and  m width/length of grid cell "unit" size
print("test 3 using printGrid(n, m) function with 2 params, n as number of cells, m as the size of each cell within the grid.\n")

print("3x3 grid with cell size m=4:")
printGrid3(3,4)
print()

print("2x2 grid with cell size m=4:")
printGrid3(2,4)
print()

print("2x2 grid with cell size m=8:")
printGrid3(2,8)
print()

