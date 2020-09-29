def print_grid_3(m,n):
    x = '+' + m*(n*' -' + ' +')
    y = m*('| ' + 2*n * ' ') + '|' 
    a = 0
    while a < m:     
        b = 0
        print(x)
        while b < n:
            print(y)
            b += 1
        a += 1
    print(x)

print_grid_3(2,3)
print_grid_3(7,5)