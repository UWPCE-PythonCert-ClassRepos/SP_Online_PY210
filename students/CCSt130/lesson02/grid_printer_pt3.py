# -*- coding: utf-8 -*-
"""
@author: Chuck Stevens :: CCSt130
Lesson02 :: Grid Printer Exercise
Part 3

Please Note: 
Column count and row count are two different variables
Column width and row height are generated using the value for column count
Created on Fri May 17 12:55:58 2019

"""
import random # PRNG used to set 'n' (width and height)
import math # so that we may round down

# runs any function n times, used in this case to create rows
def make_row(func, n):

    # counter controls row width
    # round down when 'n' is an odd number
    # round down for symmetry and avoid float
    i = math.floor(n/2)
            
    while(i >= 1):
        func(n) # calling (make_vert_border) function!
        i-=1
        
# function that prints top, middle and bottom borders
def make_horiz_border(n): # take a param for column width

    # assigning english words to symbols to make concatenation easier to read
    plus = '+'
    minus = '-'
    space = ' '

    i = n # column count for horizontal border
    
    print(plus, end='') # print left corner
    
    while(i >= 1): 
        # column width proportional
        if(n % 2 == 0): # is 'n' an even number?
            # removing extra space if 'n' is an even number
            # printing the entire border at once if 'n' is even, for symmetry
            print((space + minus)*(math.floor(n/2)) + plus, end='') # round down
            print((minus + space)*(math.floor(n/2)) + plus, end='') # round down
            # decrementing by 2 as above 2 lines print entire border
            i-=2            
        else:
            # odd number
            print((space + minus)*(math.floor(n/2)) + space + plus, end='') # round down
            # decrementing by 1 as 1/2 of border printed per loop
            i-=1

    print()
        
# function that makes (borders for) rows
# param corresponds to column width
def make_vert_border(n):
    
    # assigning English words to symbols to make concatenation easier to read    
    pipe = '|'
    space = ' '

    i = n # 'n' column count for vertical borders
    
    while(i >= 0): # to have n columns, you need n+1 vertical borders
        print(pipe + (space*(n)), end='')
        i-=1

    print()

# function that launches above functions to print the grid
def create_grid(x, y):
    
    i = y # counter controls number of rows

    # Displaying pseudo-randoms generated
    print("\nNumber of Columns Generated: %d!" % (x))
    # print("\nColumn Width is: %d!" % (n))
    print("Number of Rows Generated: %d!" % (y))
    # print("Row width is: %d!" % (n))
    print()

    while(i >= 1):        
        make_horiz_border(x) # 'x' determines column width
        make_row(make_vert_border, x) # 'x' determines width between vertical border
        i-=1

    make_horiz_border(x) # repeated for bottom border--can't include in loop

### Program entry point! ###
### Call using PRNG for x, y ###
create_grid(random.randint(3,12), random.randint(3,12))

### End ###