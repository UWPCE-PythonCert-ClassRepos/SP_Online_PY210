#! /usr/bin/env python3

#PART 1:
# Write a function that draw  a grid from the exercise
x = 4

def grid(x):
    pipe = '|'
    plus = '+'
    space = x * ' '
    dash = x * '-'
    print(plus, dash, plus, dash, plus)
    for i in range(x):
         print(pipe, space, pipe, space, pipe)

    print(plus, dash, plus, dash, plus)

    for i in range(x):
         print(pipe, space, pipe, space, pipe)
    print(plus, dash, plus, dash, plus)

grid(x)




#PART 2:
# Write a function print_grid(n) that takes on integer argument 
# print a grid just like before. BUT the side of the grid is given 
# by given argument. 

def print_grid(x):
    pipe = '|'
    plus = '+'
    space = x * ' '
    dash = x * '-'
    print(plus, dash, plus, dash, plus)
    for i in range(x):
         print(pipe, space, pipe, space, pipe)

    print(plus, dash, plus, dash, plus)

    for i in range(x):
         print(pipe, space, pipe, space, pipe)
    print(plus, dash, plus, dash, plus)


print_grid(3)
print_grid(15)



# PART 3: 
# Write a function that draws a similar grid with a specified number of rows and columns, 
# and with each cell a given size. 

def print_grid2(nrow, ncol):
    pipe = '|'
    plus = '+'
    dash = '-'
    space = ' '
    hline = (plus + dash*(ncol))*nrow + plus
    vline = (pipe + space*(ncol))*nrow + pipe
    print(hline)
    print(vline)
    for i in range(0, nrow):
        for j in range(0, ncol):
            print(vline)
        print(hline)

print_grid2(3,4)
print_grid2(5,3)






