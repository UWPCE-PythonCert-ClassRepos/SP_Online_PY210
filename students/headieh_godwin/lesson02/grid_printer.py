#PART 1
print('Part 1')

def grid():

    column = '+' + ' -' * 4 + '+' + ' -' * 4 + '+'
    rows = '|' + ' ' * 8 + '|' + ' ' * 8 + '|'

    print (column)
    print (rows)
    print (rows)
    print (rows)
    print (rows)
    print (column)
    print (rows)
    print (rows)
    print (rows)
    print (rows)
    print (column)

grid()

#PART 2
print('Part 2')

def print_grid(n):
    
    time = int(round((n-1)/2))
    rows = '+' + ' -' * time + ' +' + ' -' * time + ' +'
    column = '|' + '  ' * time + ' |' + '  ' * time + ' |'
    
    for i in range (2):
        print (rows)
        for j in range (time):
            print(column)
    print(rows);

print_grid(15)

#PART 3
print('Part 3')
def print_grid2(n,m):
    rows = '+' + (' -'* m+ ' +')*n
    column = ('| ' + '  ' * m)*(n+1)
    
    for i in range (n):
        print (rows)
        for j in range (m):
            print(column)
    print(rows);

print_grid2(3,4)
print_grid2(5,3)



