#Part 1
#print a beam followed by 4 sets of columns, twice, then a final print_beam
plus = '+ '
minus = '- '
bar = '| '
space = ' ' #number of spaces = number of minuses plus 1

def grid():

    beam = plus + 4 * minus + plus + 4 * minus + plus
    column = bar + (2 * 4 + 1) * space + bar + (2 * 4 + 1) * space + bar

    for i in range(2):
        print(beam)
        for j in range(4):
            print (column)
    print(beam)

#Part 2
#Create function that takes argument n and prints grid of size n
# n = 2 * bar + 1, therefore bar = (n-1)/2
#space = n - 1
def beam(n):
    a = (n-1)//2 * minus
    return plus + a + plus + a + plus

def column(n):
    return bar + (n-1) * space + bar + (n-1) * space + bar

def print_grid(n):
    for i in range(2):
        print(beam(n))
        for j in range((n-1)//2):
            print(column(n))
    print(beam(n))

#part 3
#print (m, n) grid with m rows and columns and n minuses and bars

def stretch(m, n):
    return m * (plus  + n * minus) + '+'

def column2(m, n):
    return m * (bar + 2*n * space) + '|'

def print_grid2(m, n):
    for i in range(m):
        print(stretch(m, n))
        for j in range(n): #need m columns w/ n bars
            print(column2(m,n))
    return(stretch(m, n))
