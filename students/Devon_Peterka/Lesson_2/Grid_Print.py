#!/usr/bin/env python3

print('Part 1 - Explicit Grid Printing without using function')
print('+ ' + 4*'- ' + '+ ' + 4*'- ' + '+')
for i in range(0,4):
    print('|' + 9*' ' + '|' + 9*' ' + '|')
print('+ ' + 4*'- ' + '+ ' + 4*'- ' + '+')
for i in range(0,4):
    print('|' + 9*' ' + '|' + 9*' ' + '|')
print('+ ' + 4*'- ' + '+ ' + 4*'- ' + '+')
print()




#Part 2 - Print grid of arbitrary cell size using a function

def print_grid(n):
    for i in range(0,n+2):
        if i in [0,n//2+1,n+1]:
            for j in range(0,2*n+3):
                if j in [0, n+1, 2*(n+1)]:
                    print('+', end='')
                elif j%2 != 0:
                    print(' ', end='')
                else:
                    print('-', end='')
        else:
            for j in range(0, 2*n+3):
                print('|', end='') if j in [0,n+1,2*(n+1)] else print(' ', end='')
        print()

print('Part 2 - Print grid using function for abitrary size')
print('\n    grid of size 3')
print_grid(3)
print('\n    grid of size 15')
print_grid(15)
print('\n    grid of size 12')
print_grid(12)



#Part 3 - Print square grid of arbitrary size and cells
def print_grid2(c, n):
    for i in range(0, c*(n+1)+1):
        for j in range(0, c*(n+1)+1):
            if i%(1+n) == 0:
                print(' +', end='') if j%(1+n) == 0 else print(' -', end='')
            else:
                print(' |', end='') if j%(1+n) == 0 else print('  ',end='')
        print()

print('\nPart 3 - Print square grid of user-defined cell size and number')
print('\n3 square grid, 4 units/square')
print_grid2(3,4)
print('\n5 square grid, 3 units/square')
print_grid2(5,3)
print('\n4 square grid, 2 units/square')
print_grid2(4,2)
print()
