# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:42:59 2020

@author: miriam
"""
# Printing a grid part 1
n= 1
m= 4

plus= '+'
minus= ' -'
wall='|'
space= '  '
def line():
    print(n*plus,m*minus,n*plus, m*minus,n*plus)
def other():
    print(n*wall,m*space,n*wall,m*space,n*wall)
    print(n*wall, m*space, n*wall, m*space, n*wall)
    print(n*wall, m*space, n*wall, m*space, n*wall)
    print(n*wall, m*space, n*wall, m*space, n*wall)
line()
other()
line()
other()
line()

# Printing a grid part 2
plus= '+'
minus= '-'
wall='|'
space= ' '
def print_grid(l):
    Newl=l+2
    for j in range(Newl):
        if j == 0 or j == int(Newl/2) or j == Newl -1:
            for i in range(Newl):
                if i == 0 or i == int(Newl/2):
                    print (plus, end = space)
                elif i == Newl - 1:
                    print (plus)
                else:
                    print (minus, end = space) 
                
        else:
            for i in range(Newl):
                if i == 0 or i == int(Newl/2):
                    print (wall, end = space)
                elif i == Newl - 1:
                    print (wall)
                else:
                    print (space, end = space)
print_grid(3)
print_grid(15)


# A Function with two parameters part 3

plus= '+'
minus= '-'
wall='|'
space= ' '

def print_grid2(rc, l):
    s = rc*l + (rc+1)
    for j in range(s):
        if j == 0 or j%(l+1)==0:
            for i in range(s):
                if i == s -1:
                    print (plus)
                elif i == 0 or i%(l+1)==0:
                    print (plus, end = space)
                else:
                    print (minus, end = space)
        else:
            for i in range(s):
                if i == s -1:
                    print(wall)
                elif i == 0 or i%(l+1)==0:
                    print (wall, end = space)
                else:
                    print(space, end = space)
                    
print_grid2(3,4)
print_grid2(5,3)
