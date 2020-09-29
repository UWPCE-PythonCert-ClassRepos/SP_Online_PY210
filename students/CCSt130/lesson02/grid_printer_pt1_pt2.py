# -*- coding: utf-8 -*-
"""
@author: Chuck Stevens :: CCSt130
Lesson02 :: Grid Printer Exercise
Part 1 and Part 2

Please Note: This version handles even numbers
Created on Thu May 16 16:35:56 2019

"""
import random # PRNG used to set 'n' (width and height)
import math # so that we may round down

# runs any function n times, used in this case to create rows
def make_row(func, n):

    # counter
    # round down when 'n' is an odd number
    # round down for symmetry and avoid float
    w = math.floor(n/2)
        
    while(w >= 1):
        func(n) # calling function!
        w-=1
        
# function that prints top, middle and bottom borders
def make_horiz_border(n): # take a param for column width

    # assigning english words to symbols to make concatenation easier to read
    plus = '+'
    minus = '-'
    space = ' '
                
    x = 2 # counter value limits to two columns
    
    print(plus, end='') # print left corner
    
    while(x >= 1): 
        # column width proportional
        if(n % 2 == 0): # is 'n' an even number?
            # removing extra space if 'n' is an even number
            # printing the entire border at once if 'n' is even, for symmetry
            print((space + minus)*(math.floor(n/2)) + plus, end='') # round down
            print((minus + space)*(math.floor(n/2)) + plus, end='') # round down
            # decrementing by 2 as above 2 lines print entire border
            x-=2            
        else:
            # odd number
            print((space + minus)*(math.floor(n/2)) + space + plus, end='') # round down
            # decrementing by 1 as 1/2 of border printed per loop
            x-=1

    print()
        
# function that makes (borders for) rows
# param corresponds to column width
def make_vert_border(n):
    
    # assigning English words to symbols to make concatenation easier to read    
    pipe = '|'
    space = ' '
        
    y = 2 # counter value limits vertical row border to two columns
    
    while(y >= 0): # to have n columns, you need n+1 vertical borders
        print(pipe + (space*(n)), end='')
        y-=1

    print()

# function that launches above functions to print the grid
def create_grid(n):
    
    z = 2 # counter value limits to two rows

    # Displaying pseudo-random generated
    print("\nColumn Width set to: %d!" % (n))
    # round (n/2) down to display row height
    print("Row Height set to: %d!" % (math.floor(n/2)))
    print()

    while(z >= 1):        
        make_horiz_border(n) # 'n' determines column width
        make_row(make_vert_border, n) # 'n' determines width between vertical border
        z-=1

    make_horiz_border(n) # repeated for bottom border--can't include in loop

### Program entry point! ###
create_grid(random.randint(3,15)) # pass pseudo-random int just for fun

