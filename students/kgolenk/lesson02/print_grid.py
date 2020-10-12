# ---------------------------------------------------------------------------- #
# Title: Lesson 02
# Description: A function that draws a grid
# ChangeLog (Who,When,What):
# Kate Golenkova, 10/05/2020, Created script
# ---------------------------------------------------------------------------- #

# Data ----------------------------------------------------------------------- #
# Declare variables
a = "-"
b = "+"
c = "|"
x = ()
y = ()
n = int
N = int
# Functions ------------------------------------------------------------------ #

# print()
# print(b, a*4, b, a*4, b, end=' ')
# print()
# print(c, " "*4, c, " "*4, c, end=' ')
# print()
# print(c, " "*4, c, " "*4, c, end=' ')
# print()
# print(c, " "*4, c, " "*4, c, end=' ')
# print()
# print(c, " "*4, c, " "*4, c, end=' ')
# print()
# print(b, a*4, b, a*4, b, end=' ')
# print()
# print(c, " "*4, c, " "*4, c, end=' ')
# print()
# print(c, " "*4, c, " "*4, c, end=' ')
# print()
# print(c, " "*4, c, " "*4, c, end=' ')
# print()
# print(c, " "*4, c, " "*4, c, end=' ')
# print()
# print(b, a*4, b, a*4, b, end=' ')
# print()

# function with one parameter
def print_grid(n):

    N = int((n - 1) / 2)
    x = (b + a * N + b + a * N + b)
    y = ("\n" + c + " " * N + c + " " * N + c)

    if n > 2:
        return x + y*N + "\n" + x + y*N + "\n" + x
    else:
        print("Please use any number > 2")

print(print_grid(7))

#function with two parameters
def print_grid2(n,m):

    x = (b + a*m)
    y = (c + " "*m)

    return ((x*n + b) + "\n" + (y*(n + 1) + "\n")*m)*n + (x*n + b)
print(print_grid2(4,5))

