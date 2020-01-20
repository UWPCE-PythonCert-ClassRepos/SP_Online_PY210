#Part 1, manual grid print
x = '+' + 4 * ' -' + ' +' + 4 * ' -' + ' +'
#x writes lines of pluses and dashes
y = '|         |         |'
#y writes lines of vertical lines

print(x)
print(y)
print(y)
print(y)
print(y)
print(x)
print(y)
print(y)
print(y)
print(y)
print(x)

#Part 2, grid print with size dependant on n
def print_grid_2(n):
    
    x = '+' + n * ' -' + ' +' + n * ' -' + ' +'
    y = '| ' + 2*n * ' ' + '|' + 2*n * ' ' + ' |'
    i=0
    print(x)
    while i < n:
        print(y)
        i += 1
    print(x) 
    i=0    
    while i < n:
        print(y)
        i += 1
    print(x)

print_grid_2(8)
print_grid_2(3)
print_grid_2(0)

#Part 3, grid size dependant on n and rows/columns dependant on m
def print_grid_3(n,m):
    x = '+' + m*(n*' -' + ' +')
    y = m*('| ' + 2*n * ' ') + '|' 
    j = 0
    while j < m:     
        i = 0
        print(x)
        while i < n:
            print(y)
            i += 1
        j += 1
    print(x)

print_grid_3(2,3)
print_grid_3(7,5)

