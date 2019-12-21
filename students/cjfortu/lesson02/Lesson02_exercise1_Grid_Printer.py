#!/usr/bin/env python

print("""Grid Printer exercise

part1()
print_grid(arg1)
print_grid2(arg2,arg3))

All entries must be real integers.
Non-real integer entries will return a correction message.

arg1 must also be an odd number.
Even numbers will return a correction message.

Negative numbers are ok.""")

import math

def part1():
    cells=2
    size=4
    print_grid2(cells,size)

def print_grid(dim):
    dimtype=type(dim)
    if dimtype!=int:
        print('entry was',dimtype,'.')
        print('entry must be a real integer')
    elif dim%2==0:
        print('entry was even.')
        print('entry must be an odd number')
    else:
        absdim=abs(dim)
        Pcells=2
        Psize=math.floor(absdim/2)
        print_grid2(Pcells,Psize)

def print_grid2(cells,size):
    celltype=type(cells)
    sizetype=type(size)
    if (celltype!=int) or (sizetype!=int):
        print('entry was',celltype,'and',sizetype,'.')
        print('both entries must be real integers')
    else:
        abscells=abs(cells)
        abssize=abs(size)
        rowsI=rowsinclusive(abscells,abssize)
        columnsE=columnsexclusive(abscells,abssize)
        for c in range(abscells):
            print(rowsI)
            for s in range(abssize):
                print(columnsE)
        if cells!=0:
            print(rowsI)
        else:
            pass


def rowsinclusive(Rcells,Rsize):
    chunk=''
    for c in range(Rcells):
        plusonleft='+ '
        minuses=Rsize*'- '
        chunk+=plusonleft+minuses
    plusonright='+'
    return chunk+plusonright

def columnsexclusive(Ccells,Csize):
    chunk=''
    for c in range(Ccells):
        leadminus='| '
        spaces=Csize*'  '
        chunk+=leadminus+spaces
    lastminus='|'
    return chunk+lastminus