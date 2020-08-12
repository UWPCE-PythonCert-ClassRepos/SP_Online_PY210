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

  
  