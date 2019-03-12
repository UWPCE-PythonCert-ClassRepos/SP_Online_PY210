#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:53:16 2019

@author: humberto gonzalez
"""

import math


### Print Grid Function ###

def print_grid():
    plus = '+'
    bar = '|'
    dash = '-' 
    space = ' '
    operatorLine = plus+space+(dash+space)*4+plus+space+(dash+space)*4+plus
    dividerLine = bar+space*9+bar+space*9+bar
    print(operatorLine)
    print(dividerLine)
    print(dividerLine)
    print(dividerLine)
    print(dividerLine)
    print(operatorLine)
    print(dividerLine)
    print(dividerLine)
    print(dividerLine)
    print(dividerLine)
    print(operatorLine)
   

### Print General Grid Function ###

def print_grid(n):
    if n<3:
        n = 3 #smallest gri possible
    
    lines = math.floor(n/2)
    
    plus = '+'
    bar = '|'
    dash = '-' 
    space = ' '
    operatorLine = plus+space+(dash+space)*lines+plus+space+(dash+space)*lines+plus
    dividerLine = bar+space*n+bar+space*n+bar
    print(operatorLine)
    for i in range(lines):
        print(dividerLine)
    print(operatorLine)
    for i in range(lines):
        print(dividerLine)
    print(operatorLine)
    

### Print General Grid Function with tw0 ###

def print_grid2(n,m):
    plus = '+'
    bar = '|'
    dash = '-' 
    space = ' '
    
    opLine = (plus+space+(dash+space)*m)*n + plus
    divLine = (bar+(space*2*m)+space)*n+bar
    
    for i in range(n):
        print(opLine)
        for i in range(m):
            print(divLine)
    
    print(opLine)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    